import json
from typing import Annotated
from annotated_types import Gt, Len
from pydantic import BaseModel
import logging
logging.basicConfig(
    filename="json_validation_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Program started")
class User(BaseModel):
    A1: Annotated[int, Gt(0)]
    B1: Annotated[str, Len(1, 20)]
    A2: Annotated[int, Gt(0)]
    B2: Annotated[str, Len(1, 20)]
    A3: str   # this will contain "*"
    B3: str
try:
    with open("three_pairs_star.json","r") as f:
        external_data = json.load(f)
    logging.info("json data is loaded to external_data")
except Exception as e:
    logging.error(f"Error loading JSON file: {e}")
try:
    logging.info("validation started")
    c = User(**external_data)
    logging.info("Validation successful")
    print(c.B1)
except ValidationError as e:
    logging.error(f"validation failed: {e}")
    print("Value is not valid")