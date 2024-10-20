from pprint import pprint
from hoshimiru import getConstellationData, findConstellations, trackConstellationLocations
from iotutils import getCurrentTimeStamp

apiToken=""
lat = 42.0
lon = -71.0

# constrellation IDs:
# 83 Ursa Major
# 60 Orion
# 46 Leo
# 86 Virgo
# 14 Cassiopea
    
for hr in [19, 20, 21, 22, 23]:
    constellation = trackConstellationLocations(83, lat, lon, 
                                                "2024-04-28", str(hr), "00",
                                                apiToken)
    if constellation != None:
        print(str(hr), ":00: ", "Pitch ", constellation[0]["altitudeNum"],
              "Direction ", constellation[0]["directionNum"], constellation[0]["direction"])

