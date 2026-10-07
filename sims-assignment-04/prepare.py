"""prepare.py: cut the raw park data down to Madison Square Park.

Reads data/Original (never edited), writes data/Processed.
All distances are in feet (EPSG:2263, NY State Plane Long Island).
"""
import json
import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString

ORIG = "data/Original/"
PROC = "data/Processed/"
FEET = 2263  # projected system, units are feet
LONLAT = 4326

# 1. Park boundary: one polygon, the legal edge of Madison Square Park.
park = gpd.read_file(ORIG + "parks_properties_madison_square_park.geojson").to_crs(FEET)
print(f"1. park boundary rows: {len(park)}  (area {park.area.iloc[0] / 43560:.2f} acres; NYC Parks says 6.234)")
boundary = park.geometry.iloc[0]

# 2. Trees: every tree record in the box around the park.
raw = json.load(open(ORIG + "forestry_tree_points_box.json"))
trees = pd.DataFrame(raw)
trees["lon"] = trees["location"].apply(lambda g: g["coordinates"][0])
trees["lat"] = trees["location"].apply(lambda g: g["coordinates"][1])
trees = gpd.GeoDataFrame(
    trees[["objectid", "genusspecies", "dbh", "tpstructure", "tpcondition"]],
    geometry=gpd.points_from_xy(trees["lon"], trees["lat"]), crs=LONLAT,
).to_crs(FEET)
print(f"2. tree records in the box around the park: {len(trees)}")

# 3. Keep only trees inside the park boundary.
inside = trees[trees.within(boundary)].copy()
print(f"3. trees inside the park boundary: {len(inside)}  (dropped {len(trees) - len(inside)} outside, mostly street trees)")
print("   status inside the park:", inside["tpstructure"].value_counts().to_dict())

# 4. Keep only living, standing trees: status 'Full'. They are the only ones that cast shade.
full = inside[inside["tpstructure"] == "Full"].copy()
print(f"4. trees with status Full (the shade trees): {len(full)}  (dropped {len(inside) - len(full)} Retired/Stump/Shaft)")

# 5. Footpaths: every OpenStreetMap path segment in the box around the park.
osm = json.load(open(ORIG + "osm_footways_box.json"))["elements"]
rows = [
    {
        "osm_id": e["id"],
        "highway": e["tags"].get("highway"),
        "footway": e["tags"].get("footway", ""),
        "geometry": LineString([(p["lon"], p["lat"]) for p in e["geometry"]]),
    }
    for e in osm
]
paths = gpd.GeoDataFrame(rows, crs=LONLAT).to_crs(FEET)
print(f"5. path segments in the box around the park: {len(paths)}")

# 6. Drop street sidewalks and crossings; they belong to the street, not the park.
paths = paths[~paths["footway"].isin(["sidewalk", "crossing", "traffic_island"])]
print(f"6. path segments that are not sidewalks or crossings: {len(paths)}")

# 7. Keep the part of each path that lies inside the park boundary.
paths["geometry"] = paths.intersection(boundary)
paths = paths[~paths.geometry.is_empty]
print(f"7. path segments with some part inside the park: {len(paths)}  (total length {paths.length.sum():,.0f} ft)")

# 8. The student's hand-drawn path (data/Original/observed_path_drawing.png), read off by eye.
#    Pixels in the screenshot are fitted to 4 landmarks (park corner, park tip, two circles) whose map positions
#    in feet were read from the park data. Illustration, not observed data.
import numpy as np
pix = np.array([[547, 133], [598, 830], [630, 350], [522, 598]], float)
landmark_ft = np.array([[987545, 210085], [987570, 209258], [987640, 209830], [987497, 209508]], float)
M = np.linalg.lstsq(np.c_[pix, np.ones(4)], landmark_ft, rcond=None)[0]
red = np.array([[568, 148], [572, 178], [590, 238], [603, 275], [625, 332], [610, 372], [640, 395], [648, 440],
                [650, 490], [645, 522], [625, 550], [580, 578], [525, 580], [498, 600], [490, 645], [490, 690],
                [515, 718], [551, 712], [570, 758], [580, 778]], float)
observed = np.c_[red, np.ones(len(red))] @ M
print(f"8. hand-drawn observed path: {len(observed)} points, {LineString(observed).length:,.0f} ft long")

# 9. Write the one file the page embeds. Coordinates are feet east/north of the park's south-west corner.
minx, miny, _, _ = boundary.bounds
def shift(xy):
    return [[round(x - minx, 1), round(y - miny, 1)] for x, y in xy]
lines = []
for g in paths.geometry:
    for part in (g.geoms if hasattr(g, "geoms") else [g]):
        if part.geom_type == "LineString":
            lines.append(shift(part.coords))
out = {
    "units": "feet",
    "origin_epsg2263": [minx, miny],
    "boundary": shift(boundary.geoms[0].exterior.coords if hasattr(boundary, "geoms") else boundary.exterior.coords),
    "paths": lines,
    "trees": shift([(p.x, p.y) for p in full.geometry]),
    "observed": shift(observed),
}
json.dump(out, open(PROC + "park.json", "w"))
print(f"9. wrote data/Processed/park.json: {len(out['paths'])} path lines, {len(out['trees'])} trees, "
      f"{len(out['boundary'])} boundary points, {len(out['observed'])} observed points")
