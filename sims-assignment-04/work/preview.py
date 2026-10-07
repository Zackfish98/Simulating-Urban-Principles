import geopandas as gpd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
P="data/Processed/"
b=gpd.read_file(P+"park_boundary.geojson").to_crs(2263)
t=gpd.read_file(P+"trees_full.geojson").to_crs(2263)
p=gpd.read_file(P+"park_paths.geojson").to_crs(2263)
fig,ax=plt.subplots(figsize=(7,10))
b.boundary.plot(ax=ax,color="k")
t.plot(ax=ax,color="green",markersize=8,alpha=.6)
p.plot(ax=ax,color="tab:blue",linewidth=1.5)
ax.set_aspect("equal"); ax.set_title("Madison Square Park: paths (blue), Full trees (green)")
fig.savefig("work/preview.png",dpi=90,bbox_inches="tight")
print(b.total_bounds)
