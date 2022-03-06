import random
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import numpy as np


def get_data_querys(query_info):
    org = "jirs28"
    token = "CogeqAhxfHt5o-0rkeCtKiMxyhXMjJaqugbHUN_LisF7cvH9LaIyDvFAZfU5CEDVrFkiYeh_69_TQ-NKUsKCeg=="
    url = "https://us-east-1-1.aws.cloud2.influxdata.com"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )
    query_api = client.query_api()
    query_T = query_info

    result1 = query_api.query(org=org, query=query_T)
    arr_tiempo = []
    for table in result1:
        for record in table.records:
            arr_tiempo.append((record.get_value()))
    ar_li = np.asarray(arr_tiempo).reshape(1, -1)
    return ar_li


queryTime = ' from(bucket:"ShowerS")\
        |> range(start: -30d)\
        |> filter(fn:(r) => r._measurement == "Tiempo")\
        |> filter(fn:(r) => r._field == "Segundos" ) '

# Temperatura prom
queryTemp = ' from(bucket:"ShowerS")\
       |> range(start: -30d)\
       |> filter(fn:(r) => r._measurement == "TemperaturaProm")\
       |> filter(fn:(r) => r._field == "Celsius" ) '
queryLiters = ' from(bucket:"ShowerS")\
            |> range(start: -30d)\
            |> filter(fn:(r) => r._measurement == "Litros")\
            |> filter(fn:(r) => r._field == "Litros" ) '

queryTime = ' from(bucket:"ShowerS")\
        |> range(start: -30d)\
        |> filter(fn:(r) => r._measurement == "Tiempo")\
        |> filter(fn:(r) => r._field == "Segundos" ) '


#####################
# Temperatura prom
queryTemp15 = ' from(bucket:"ShowerS")\
       |> range(start: -18h, stop: -15h)\
       |> filter(fn:(r) => r._measurement == "TemperaturaProm")\
       |> filter(fn:(r) => r._field == "Celsius" ) '

queryLiters15 = ' from(bucket:"ShowerS")\
            |> range(start: -18h, stop: -10h)\
            |> filter(fn:(r) => r._measurement == "Litros")\
            |> filter(fn:(r) => r._field == "Litros" ) '

queryTime15 = ' from(bucket:"ShowerS")\
        |> range(start: -18h, stop: -10h)\
        |> filter(fn:(r) => r._measurement == "Tiempo")\
        |> filter(fn:(r) => r._field == "Segundos" ) '


print("Tiempos")
Tim = get_data_querys(queryTime15)
print("Temperaturas")
Celsius = get_data_querys(queryTemp15)
print("Litros")
Lits = get_data_querys(queryLiters15)
promTim = round((np.sum(Tim))/60, 2)
print("Minutos de baño : ", promTim)
# obtain()
