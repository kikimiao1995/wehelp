import urllib.request as request
import json
import re

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
  data = json.load(response)

spots=data["result"]["results"]

with open("data.csv", "w") as file:
  imgRule = '(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)'
  districtRule = '\s([\u4E00-\u9FFF]{3})'
  for spot in spots:
    if int(spot["xpostDate"][0:4]) >= 2015:
      firstImg = re.search(imgRule, spot["file"], re.I).group() # re.I = ignore case
      district = re.search(districtRule, spot["address"]).group(1)
      file.write(f"{spot['stitle']},{district},{spot['longitude']},{spot['latitude']},{firstImg}\n")