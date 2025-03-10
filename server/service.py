import json
import os
from fastapi import HTTPException
from typing import List


def read_profit_and_loss_data(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found")
    with open(file_path, "r") as file:
        data = json.load(file)
        return data