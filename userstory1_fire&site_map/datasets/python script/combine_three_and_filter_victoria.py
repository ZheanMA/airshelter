import pandas as pd
import geopandas as gpd
from shapely.geometry import Point,Polygon
# read three csv satellites dataset into python, you need change it to your path
read_MODIS = pd.read_csv("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\past 7d fire data\\MODIS_C6_Australia_NewZealand_7d.csv")
read_SUOMI_VIIR = pd.read_csv("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\past 7d fire data\\SUOMI_VIIRS_C2_Australia_NewZealand_7d.csv")
read_J1_VIIR = pd.read_csv("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\past 7d fire data\\J1_VIIRS_C2_Australia_NewZealand_7d.csv")
# add one column use to save source
read_MODIS["source"] = "MODIS"
read_SUOMI_VIIR["source"] = "SUOMI VIIR"
read_J1_VIIR["source"]="J1 VIIR"
# combine three dataset together
seven_day_fire = pd.concat([read_MODIS, read_SUOMI_VIIR,read_J1_VIIR])
seven_day_fire = seven_day_fire.reset_index()
del seven_day_fire["index"]
# read vic shapefile use to filter the bushfire happens in Victoria
victoria_map = gpd.read_file("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\VIC_STATE_POLYGON_shp")
vic_seven_day_fire_list = columns=seven_day_fire.columns.tolist()
vic_seven_day_fire = pd.DataFrame(columns=vic_seven_day_fire_list)
for i in range(0,len(seven_day_fire)):
    point = Point(seven_day_fire.loc[i,"longitude"],seven_day_fire.loc[i,"latitude"])
    # judgment the camping site point within the bush fire area
    records = victoria_map.geometry.contains(point)
    if pd.Series(records).any() == True:
        vic_seven_day_fire=vic_seven_day_fire.append(pd.Series(seven_day_fire.loc[i].tolist(), index=vic_seven_day_fire_list),ignore_index=True)
# save it into your path
vic_seven_day_fire.to_csv("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\past 7d fire data\\vic_fire_data.csv", index=False)