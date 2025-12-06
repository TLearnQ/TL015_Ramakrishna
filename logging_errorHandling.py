import json
import logging
logging.basicConfig(
    filename="error_detection.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Program started")
with open("nested.json", "r") as f:
    data = json.load(f)
logging.info("json loadedd to data")
try:
    logging.info("checking for erors")
    for keys in data:
        if keys == "error":
            with open("Error.json", "w") as l:
                json.dump(keys.value(), l)
                logging.info(f"error detected is {keys.value()}")
except:
    print("try again")
    logging.info("Compilation error occured")
    