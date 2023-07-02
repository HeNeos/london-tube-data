# London lines

## Data schema

### stations

| stationId    | stationName | longitude | latitude  |
|--------------|-------------|-----------|-----------|
| 9400ZZLUBNK8 | Bank        | -0.091397 | 51.512884 |
| 940GZZLUACY  | Archway     | -0.134819 | 51.565478 |
| 940GZZLUACT  | Acton Town  | -0.280462 | 51.503057 |

### tubeLines

| lineName     |
|--------------|
| Bakerloo     |
| Central      |
| Circle       |

### stationLines

| stationId    | lineName     |
|--------------|--------------|
| 940GZZLUBST  | Bakerloo     |
| 940GZZLUCHX  | Bakerloo     |
| 940GZZLUBKE  | Central      |

## Requisites

Install `mysql.connector`:
```
pip install mysql-connector-python
```

## How to use

1. Run `create_tables.py` to read the `train-network.json` file to create the tables.
2. Run `query.py` to execute the two type of queries:
    1. Type `help` to get more information about the queries:
    ```sh
    q1 [station_id_1, station_id_2, ...]
    q1 [station_name_1, station_name_2, ...]
    q2 [line_name_1, line_name_2, ...]
    ```
    2. Type `exit` to quit.
