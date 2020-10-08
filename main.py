import fire

from typing import List

from fintools.settings import get_logger
from fintools.utils import timeit
from fintools.utils import method_caching


logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    @method_caching
    def element(self, position: int) -> int:
        return position if (position < 2) else \
            self.element(position - 1) + self.element(position - 2)

    @timeit(logger=logger)
    def sequence(self, length: int) -> List[int]:
        value = list(self.element(position=i) for i in range(0, length))
        return value


if __name__ == "__main__":
    fire.Fire(Main)
    