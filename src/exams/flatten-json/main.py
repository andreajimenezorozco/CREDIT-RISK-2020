import json
from fintools.settings import get_logger

def show(self, file):
    logger.info("Calling the show method.")
    with open(file, "r") as f:
        content = json.loads(f.read())
        return content

def flatten(file):
    with open(file, "r") as f:
        info = json.loads(f.read())
    return flatten_json(info)





