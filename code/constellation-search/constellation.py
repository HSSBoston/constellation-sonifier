from pprint import pprint
from hoshimiru import getConstellationData, findConstellations
from iotutils import getCurrentTimeStamp

lat = 42.0
lon = -71.0
apiToken=""

dateTime = getCurrentTimeStamp().split("-")

constellationsList = getConstellationData(lat, lon,
                                          dateTime[0] + "-" + dateTime[1] + "-" + dateTime[2],
                                          dateTime[3], dateTime[4],
                                          apiToken)
print(len(constellationsList), "constellations viewable")
# pprint(constellationsList)

bearing = 180
pitch = 65

foundConstellations = findConstellations(constellationsList, bearingDecimal=bearing, pitchDecimal=pitch)
print(len(foundConstellations), "constellations viewable at bearing=", bearing, "pitch=", pitch)
pprint(foundConstellations)

# sConstellations = [
#     [c["enName"], c["jpName"], c["id"], c["season"],
#      c["direction"], c["directionNum"], c["altitude"], c["altitudeNum"],
#      c["content"], c["origin"],c["starImage"] ]
#     for c in constellationsList if c["directionNum"] >= 90 and c["directionNum"] <= 270 ]
# print("South:", len(sConstellations), "constellations vewable")
# pprint(sConstellations)
# 
# nConstellations = [
#     [c["enName"], c["jpName"], c["id"], c["season"],
#      c["direction"], c["directionNum"], c["altitude"], c["altitudeNum"],
#      c["content"], c["origin"],c["starImage"] ]
#     for c in constellationsList if c["directionNum"] > 270 or c["directionNum"] < 90 ]
# print("North", len(nConstellations), "constellations vewable")
# pprint(nConstellations)

