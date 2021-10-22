# Conversion script for LogAir API data to GeoJSON
# Requires Python 3
#
# Usage: 
# 1. Save your API output data to a local file,
#    and call it "LogAirData.json"
# 2. Put this script in the same folder, and run it!
# 3. You will get a "LogAir.geojson" as an output

from io import open
import json

thefile = open('LogAirData.json', 'r')
thejson = json.load(thefile)

thedata = []
for row in thejson:
    lat = row["latitude"]
    lon = row["longitude"]
    if not lat or not lon:
        continue
    del(row["latitude"])
    del(row["longitude"])
    del(row["extra_data"])
    del(row["pm_1"])
    del(row["pm_4"])
    del(row["mobile_api_key_id"])
    thedata.append((
        lon, lat, row
    ))


geofeatures = [ {"type": "Feature",
              "geometry": {
                  "type": "Point",
                  "coordinates": [lon, lat]
              },
              "properties": props }
              for lon, lat, props in thedata ] 
geojson = {
  "type": "FeatureCollection",
  "features": geofeatures
}

with open("LogAir.geojson", "w") as fn:
    fn.write(json.dumps(geojson))
