###-----------------------第一題-----------------------###

import json
import csv
from urllib.request import urlopen
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
response = urlopen(url)
data = json.loads(response.read())

content = open("data.csv","w",encoding="utf_8_sig")


for first_DicValue in data.values():
    for Second_DicValue in first_DicValue.values():
        if type(Second_DicValue) == list:
            for listValue in Second_DicValue:
                site = listValue['stitle']
                region = listValue['address'][5:8]
                longitude = listValue['longitude']
                latitude = listValue['latitude']
                file = listValue['file']
                picture = "https://"+file.split("https://")[1]
                ymd = listValue['xpostDate'].split('/')[0]
                if ymd >= '2015':
                    print(site,region,longitude,latitude,picture,sep = ",",end="\n",file=content)
content.close()

