import pandas as pd
import geopandas as gpd
campingsite_data = gpd.read_file("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\Recreation Sites\\recweb_site.shp")
campingsite_data_col = campingsite_data.columns.tolist()
filted_new_camping_data = pd.DataFrame(columns=campingsite_data_col)
for i in range(0,len(campingsite_data)):
    if campingsite_data.loc[i,"CAMPING"] == "Y":
        filted_new_camping_data=filted_new_camping_data.append(pd.Series(campingsite_data.loc[i].tolist(), index=campingsite_data_col),ignore_index=True)
filted_new_camping_data.to_csv("E:\\Study\\20 semester 1\\Project\\bushfire\\victoria\\recreate_data(only_camping_site)\\recweb_site.csv")