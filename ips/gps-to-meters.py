# py -m pip install <package>
from pyproj import Proj, Transformer

print(Proj.__name__)

# Define a transformer from WGS84 (EPSG:4326) to UTM or another meter-based CRS
transformer = Transformer.from_crs("EPSG:4326", "EPSG:32633", always_xy=True)

# Example coordinates (longitude, latitude)
lon, lat = -80.545065, 43.47798167

# Convert to meters
x, y = transformer.transform(lon, lat)

print(f"Coordinates in meters: x={x}, y={y}")
