# Task 1: Print out all the lines across a station (name)
# Task 2: Print out all the stations (name) for a particular line
# 

import mysql.connector
import os
import json

f = open('train-network.json')
data = json.load(f)

def delete_table(cursor, table_name):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def create_station_sql():
    table_name = "stations"
    delete_table(cursorObject, table_name)

    header = f"CREATE TABLE {table_name}(\n"
    header += "stationId VARCHAR(12) NOT NULL PRIMARY KEY\n"
    header += ",stationName VARCHAR(33) NOT NULL\n"
    header += ",longitude NUMERIC(9,6) NOT NULL\n"
    header += ",latitude NUMERIC(9,6) NOT NULL\n"
    header += ");"

    cursorObject.execute(header)

    query = f"INSERT INTO {table_name}(stationId, stationName, longitude, latitude) VALUES (%s, %s, %s, %s)"

    for station in data["stations"]:
        values = (
            station["id"],
            station["name"],
            station["longitude"],
            station["latitude"]
        )
        cursorObject.execute(query, values)

    dataBase.commit()

def create_lines_sql():
    table_name = "tubeLines"
    delete_table(cursorObject, table_name)
    
    header = f"CREATE TABLE {table_name}(\n"
    header += "lineName VARCHAR(33) NOT NULL PRIMARY KEY\n"
    header += ");"

    cursorObject.execute(header)

    query = f"INSERT INTO {table_name}(lineName) VALUES (%s)"

    for line in data["lines"]:
        cursorObject.execute(query, (line["name"],))

    dataBase.commit()

def create_stationLine_sql():
    table_name = "stationLines"
    delete_table(cursorObject, table_name)

    header = f"CREATE TABLE {table_name}(\n"
    header += "stationId VARCHAR(12) NOT NULL\n"
    header += ",lineName VARCHAR(33) NOT NULL\n"
    header += ",PRIMARY KEY (stationId, lineName)\n"
    header += ",FOREIGN KEY (stationId) REFERENCES stations(stationId)\n"
    header += ",FOREIGN KEY (lineName) REFERENCES tubeLines(lineName)\n"
    header += ");"

    cursorObject.execute(header)

    query = f"INSERT INTO {table_name}(stationId, lineName) VALUES (%s, %s)"

    for line in data["lines"]:
        line_name = line["name"]
        list_stations = line["stations"]
        for station in list_stations:
            values = (
                station,
                line_name
            )
            cursorObject.execute(query, values)

    dataBase.commit()


if __name__ == "__main__":
    dataBase = mysql.connector.connect(
        host="localhost",
        user="heneos",
        passwd="12345678",
        database="londonTube"
    )

    cursorObject = dataBase.cursor()

    create_station_sql()
    create_lines_sql()
    create_stationLine_sql()

    cursorObject.close()
    dataBase.close()

# STATIONS
# STATION-ID STATION-NAME LONGITUDE LATITUDE

# StationLine
# STATION-ID LINE-NAME

# LINES
# LINE-NAME