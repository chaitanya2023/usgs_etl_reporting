# Python script to query and download all earthquake events during year 2017

import requests
import json
from dotenv import load_dotenv  # for database credentials
import os 
import pandas as pd
import sqlite3
from sqlite3 import Error
import time 
from datetime import date

today = date.today()
#yyyy-mm-dd
start_date = today.strftime("%Y-%m-%d")
end_date = start_date + datetime.timedelta(days=1)

# assuming the name of earthquake database in SQlite as usgs_earthquake.db
db_file_path = 'usgs_earthquake.db'

# connect to database and open connection 
sqlite3_conn = sqlite3.connect(db_file_path)

# prepare parameter
url_param = {"format": "geojson", "starttime": start_date, "endtime": end_date, "alertlevel": "orange"}

# set parameters and send out 'get' request
site_url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
site_data = requests.get(site_url, params = url_param)

site_data_text = site_data.text
site_json = pd.read_json(site_data_text)
# export json data to csv
site_json.to_csv("../output.csv")

# read csv file 
site_csv = pd.read_csv(../output.csv)
# import csv file into event_stage table using pandas command 
orders.to_sql('event_stage', sqlite3_conn, if_exists='append', index = False, chunksize=100000)

# close the connection
sqlite3.close()
