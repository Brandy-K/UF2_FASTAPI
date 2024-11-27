import db_connect
import pandas as pd


def csv_to_json():

    df = pd.read_csv("paraules_temàtica_penjat.csv")

    d = df.to_dict(orient='list')
    return d


data = csv_to_json()

for i in range(500):
    db_connect.insert_data(i, data)
