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
