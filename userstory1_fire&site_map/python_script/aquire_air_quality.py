import urllib, urllib3, sys
import certifi 
import pandas as pd
import re
import time
# change the path to your ducument
read_camping_site = pd.read_csv("E:\\Study\\20 semester 1\\Project\\Javascript_visulization\\datasets\\recweb_site.csv")
all_lat = read_camping_site["LATITUDE"]
all_lng = read_camping_site["LONGITUDE"]
read_camping_site["pm25"]="no_data"
read_camping_site["pm10"]="no_data"
# search air quality data, find pm25 and pm10 from it
def searchairq(air_quality_data):
    air_quality = str(air_quality_data)
    pm25 = re.search(r"pm25\":{\"v\":(.*?)}", air_quality)
    pm10 = re.search(r"pm10\":{\"v\":(.*?)}", air_quality)
    try:
        return [pm25[1],pm10[1]]
    except:
        return ["no_data","no_data"]
#set api methods
host = 'https://api.waqi.info'
method = 'GET'
appcode='token=35b4c6629577904042044bbe7863d27097b18234'
# using api get data according to coordinates
for i in range(0,len(all_lng)):
    path = '/feed/geo:'+str(all_lat[i])+';'+str(all_lng[i])+'/'
    url = host+path+'?'+appcode
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    request = http.request(method, url)
    pm_data = searchairq(request.data)
    read_camping_site.loc[i,"pm25"] = pm_data[0]
    read_camping_site.loc[i,"pm10"] = pm_data[1]
# change the path to your document
read_camping_site.to_csv("E:\\Study\\20 semester 1\\Project\\Javascript_visulization\\datasets\\recweb_site_with_air_quality.csv",index=False)