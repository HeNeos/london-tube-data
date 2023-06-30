# Task 1: Print out all the lines across a station (name)
# Task 2: Print out all the stations (name) for a particular line
# 
# 

import mysql.connector
import os
import json

f = open('train-network.json')
data = json.load(f)

def create_station_sql():
    table_name = "stations"
    header = f"CREATE TABLE {table_name}(\n"
    header += "station-id VARCHAR(12) NOT NULL PRIMARY KEY\n"
    header += ",name VARCHAR(33) NOT NULL\n"
    header += ",longitude NUMERIC(9,6) NOT NULL\n"
    header += ",latitude NUMERIC(9,6) NOT NULL\n"
    header += ");"

    cursorObject.execute(header)

    for station in data["stations"]:
        name = station["name"]
        id = station["id"]
        longitude = station["longitude"]
        latitude = station["latitude"]
        row = f"INSERT INTO {table_name}(station-id,name,longitude, latitude) VALUES ('{id}','{name}',{longitude},{latitude});"
        cursorObject.execute(row)

def create_lines_sql():
    table_name = "lines"
    header = f"CREATE TABLE {table_name}(\n"
    header += "line-name VARCHAR(33) NOT NULL PRIMARY KEY\n"
    header += ",station-id VARCHAR(12) NOT NULL\n"
    header += ");"

    cursorObject.execute(header)

    for line in data["lines"]:
        line_name = line["name"]
        list_stations = line["stations"]
        for station in list_stations:
            row = f"INSERT INTO {table_name}(line-name,station-id) VALUES ('{line_name}','{station}');"
            cursorObject.execute(row)

dataBase = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="test"
)

cursorObject = dataBase.cursor()

create_station_sql()
create_lines_sql()

# STATIONS
# STATION-ID NAME LONGITUDE LATITUDE
#
#

# LINES
# LINE-NAME STATION-ID
# CIRCLE          "940GZZLUHSC,940GZZLUGHK"
#
#
