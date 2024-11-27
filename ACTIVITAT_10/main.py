from fastapi import FastAPI
import db_connect
import pandas as pd

# Initialize FastAPI app
app = FastAPI()


def csv_to_json():
    df = pd.read_csv("paraules_temàtica_penjat.cs")
    d = df.to_dict(orient='list')
    return d


# Define the endpoint to insert data
@app.get("/penjat/tematica/opcions")
async def insert_data_endpoint():
    try:

        data = csv_to_json()

        for i in range(500):
            db_connect.insert_data(i, data)
        return {"message": "Data inserted successfully"}

    except Exception as e:

        return {"error": str(e)}

