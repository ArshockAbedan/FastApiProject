import json
from typing import Union
from fastapi import FastAPI, Request, UploadFile, File
# import tensorflow as tf
# import numpy as np
from pydantic import BaseModel

# from uvicorn import run
# import os

from app.Services import calc_expected_health_premium

app = FastAPI()


class Item(BaseModel):
    lead_id: int
    marketing_rank: int
    gender: str
    age: int
    credit_score: int
    urgency: Union[str, None] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/dummy_path/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
#

@app.post("/create/")
async def create_item(item: Item):
    return item


# @app.get("check_model/{input_data}")
# def check_model(input_data: str):
#     # Recreate the exact same model, including its weights and the optimizer
#     # new_model = tf.keras.models.load_model('my_model.h5')
#     return type(input_data)
#     # # converting list to array
#     # arr = np.array(input_data)
#     # return new_model.predict(arr)


@app.post("/monthly_premium/")
def create_upload_files(upload_file: UploadFile = File(...)):
    json_data = json.load(upload_file.file)
    try:
        expected_health_premium = calc_expected_health_premium(json_data)
        rounded_expected_health_premium = round(expected_health_premium, 2)
    except ... as err:
        rounded_expected_health_premium = "General Error!"
    return rounded_expected_health_premium

# if __name__ == "__main__":
#     # Opening JSON file
#     f = open('lead_id_1.json')
#
#     # returns JSON object as
#     # a dictionary
#     data = json.load(f)
#
#     result = calc_expected_health_premium(data)
#     rounded_result = round(result, 2)
#     print(rounded_result)
#
#     # Closing file
#     f.close()
