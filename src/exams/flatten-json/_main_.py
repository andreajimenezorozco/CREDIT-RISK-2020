import fire
import logging
from .main import Main


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    fire.Fire(Main)
