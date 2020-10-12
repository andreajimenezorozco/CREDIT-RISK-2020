from .models import Borrower

from fintools.settings import get_logger

logger = get_logger(name="_main_")
DEFAULT_FILENAME = "./borrowers/candidates.json"


class Main:

    @staticmethod
    def show(file: str = DEFAULT_FILENAME) -> str:
        logger.info("Calling the show method.")
        # TODO: read file and show content
        with open(file, "r") as f:
            content = f.read()
            return content

    @staticmethod
    def insert(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):
        borrower = Borrower(email=email, age=age, income=income)
        borrower.save(file=file)

    @staticmethod
    def update(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):
        borrower = Borrower(email=email, age=age, income=income)
        borrower.update(file=file)


