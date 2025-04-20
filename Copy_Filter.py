import pandas as pd
from datetime import date, timedelta
import os
import glob

#location of downloads folder, grabbing the most recently downloaded file
list_of_files = glob.glob('C:/Downloads/*')
# * means all; if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

df = pd.read_excel(latest_file, header=8)
#Reads in the latest file which in this case will always be an excel file
df = df.iloc[1:].reset_index(drop=True)

df.to_csv("test_change.csv", index=False)
df.to_csv("test_keep.csv", index=False)
# works: splits it into 2 with first 8 gone

df_work = pd.read_csv("C:/PycharmProjects/Afternoon Process Set/test_change.csv")

df_work["Date Change Entered"] = pd.to_datetime(df_work["Date Change Entered"])
# Changes to the correct datetime interface in order to properly filter
today = date.today()
today_converted = today.strftime("%m/%d/%Y")
yesterday = today - timedelta(days=1)
yesterday_converted = yesterday.strftime("%m/%d/%Y")

#Filters for location previous and the last 2 days 
filtered_df = df_work[(df_work["Location - Previous"] == "Set value here") 
                      & (df_work["Date Change Entered"].isin([today_converted, yesterday_converted])) &
                      (df_work["Last Day Worked"].astype(str).str.strip() != "")]

filtered_df = filtered_df.dropna(subset=["Last Day Worked"])
print(filtered_df["Last Day Worked"], filtered_df["Full Name"], filtered_df["Worker ID"])
# Writes this into the correct csv file
filtered_df.to_csv("Beginning_Filter.csv", index=False)
