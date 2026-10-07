import numpy as np, json, geopandas as gpd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from shapely.geometry import LineString
# Landmarks: pixel in the screenshot -> feet on the map (read from work/preview.png and the screenshot)
pix=np.array([[547,133],[598,830],[630,350],[522,598]],float)
ft=np.array([[987545,210085],[987570,209258],[987640,209830],[987497,209508]],float)
A=np.c_[pix,np.ones(len(pix))]
M,res,_,_=np.linalg.lstsq(A,ft,rcond=None)
# Student's red line, read off the screenshot in pixels (start NW, end S tip)
red=np.array([[568,148],[572,178],[590,238],[603,275],[625,332],[610,372],[640,395],[648,440],[650,490],[645,522],[625,550],[580,578],[525,580],[498,600],[490,645],[490,690],[515,718],[551,712],[570,758],[580,778]],float)
xy=np.c_[red,np.ones(len(red))]@M
json.dump({"crs":"EPSG:2263","units":"feet","note":"Hand-drawn by the student on a Google Maps screenshot, read off by eye and fitted to 4 landmarks. Illustration, not observed data.","points":xy.round(1).tolist()},open("data/Processed/observed_path.json","w"),indent=1)
b=gpd.read_file("data/Processed/park_boundary.geojson").to_crs(2263)
p=gpd.read_file("data/Processed/park_paths.geojson").to_crs(2263)
fig,ax=plt.subplots(figsize=(7,10)); b.boundary.plot(ax=ax,color="k"); p.plot(ax=ax,color="tab:blue",lw=1.2)
ax.plot(*xy.T,color="red",lw=2); ax.plot(*xy[0],"go"); ax.plot(*xy[-1],"ro"); ax.set_aspect("equal")
fig.savefig("work/observed_preview.png",dpi=90,bbox_inches="tight")
print("landmark fit error (ft):",np.abs(A@M-ft).max().round(1), "path length ft:",round(LineString(xy).length))
