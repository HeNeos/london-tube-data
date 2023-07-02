import mysql.connector

def print_help():
    print("Types of queries:")
    print("1. Print lines across a station.")
    print("q1 [station_id_1, station_id_2, ...]")
    print("q1 [station_name_1, station_name_2, ...]\n")
    print("2. Print all the stations for a particular line.")
    print("q2 [line_name_1, line_name_2, ...]\n")

def print_lines_for_station(stations):
    invalid_stations = []
    stations_name = []
    unique_lines = set()
    stations = list(map(str.strip, stations))

    for station in stations:
        cursorObject.execute("SELECT stationName FROM stations WHERE stationId = %s", (station,))
        result = cursorObject.fetchone()
        if result:
            stations_name.append(result[0])
        else:
            cursorObject.execute("SELECT COUNT(*) FROM stations WHERE stationName = %s", (station,))
            count = cursorObject.fetchone()[0]
            if count > 0:
                stations_name.append(station)
            else:
                invalid_stations.append(station)
    
    if len(invalid_stations) > 0:
        print(f"The stations {','.join(invalid_stations)} are invalid.")
        return

    query = "SELECT lineName FROM stationLines WHERE stationId IN (SELECT stationId FROM stations WHERE stationName = %s)"

    print(f"Lines for station {', '.join(stations_name)}:")
    for station in stations_name:
        cursorObject.execute(query, (station,))
        lines = cursorObject.fetchall()
        for line in lines:
            unique_lines.add(line[0])

    print("\n".join(list(unique_lines)))

def print_stations_for_line(lines_name):
    invalid_lines = []
    lines_name = list(map(str.strip, lines_name))
    unique_stations = set()

    for line in lines_name:
        cursorObject.execute("SELECT COUNT(*) FROM tubeLines WHERE lineName = %s", (line,))
        count = cursorObject.fetchone()[0]
        if count <= 0:
            invalid_lines.append(line)
    
    if len(invalid_lines) > 0:
        print(f"The lines {','.join(invalid_lines)} are invalid.")
        return

    query = "SELECT stationName FROM stations WHERE stationId IN (SELECT stationId FROM stationLines WHERE lineName = %s)"

    print(f"Lines for station {', '.join(lines_name)}:")
    for line in lines_name:
        cursorObject.execute(query, (line,))
        stations = cursorObject.fetchall()
        for station in stations:
            unique_stations.add(station[0])

    print("\n".join(list(unique_stations)))

if __name__ == "__main__":
    dataBase = mysql.connector.connect(
        host="localhost",
        user="heneos",
        passwd="12345678",
        database="londonTube"
    )

    cursorObject = dataBase.cursor()

    print_help()

    while True:
        try:
            print(">>>", end="")
            query = input()
            if query.startswith("q1"):
                query = query[3:]
                queries = query.split(',')
                print_lines_for_station(queries)
            elif query.startswith("q2"):
                query = query[3:]
                queries = query.split(',')
                print_stations_for_line(queries)
            elif query.startswith("help"):
                print_help()
            elif query == "exit":
                break
            else:
                print("Invalid query, type 'help' for more information.")
        except (EOFError, KeyboardInterrupt):
            break

    cursorObject.close()
    dataBase.close()