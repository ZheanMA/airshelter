import pandas as pd
import geopandas as gpd
import calendar
read_path = input("Enter the path of orginal fire data(shapefile):")
save_path = input("Enter storage path:")
start_year = int(input("start year:"))
end_year = int(input("end year:"))
fire_his_data=gpd.read_file(read_path)
fire_month_count = pd.DataFrame(columns=["year","month","day"])
for i in range(0,len(fire_his_data)):
    total = list(map(int,str(fire_his_data["STRTDATIT"][i])))[0:8]
    if len(total) < 8:
        pass
    else:
        year_list = total[0:4]
        year = int("".join(str(i) for i in year_list))
        month_list = total[4:6]
        if month_list[0]==0:
            month = calendar.month_name[month_list[1]]
        else:
            month = int("".join(str(i) for i in month_list))
            try:
                month = calendar.month_name[month]
            except:
                pass
        day_list = total[6:8]
        day = int("".join(str(i) for i in day_list))
        fire_month_count = fire_month_count.append({'year' : year , 'month' : month, 'day':day} , ignore_index=True)
filte_fire_month_count= fire_month_count.loc[(fire_month_count["year"] >= start_year) & (fire_month_count["year"] =< end_year)]
filte_fire_month_count.to_csv(save_path)