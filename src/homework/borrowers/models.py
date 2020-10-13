import json
from typing import Dict

from .utils import get_current_utc


class Borrower:

    def __init__(self, email: str, age: int, income: float):
        self.created_at = get_current_utc()
        self.updated_at = self.created_at
        self.email = email
        self.age = age
        self.income = income

    def to_json(self) -> Dict:
        return {
            "email": self.email,
            "age": self.age,
            "income": self.income,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def save(self, file: str):
        # TODO: save the borrower into the json file!
        with open("./borrowers/candidates.json") as f:
            data = json.load(f)
        data["candidates"].append(self.to_json())
        data["updated_at"] = self.updated_at

        with open("./borrowers/candidates.json", 'w') as f:
            f.write(json.dumps(data, indent=4))

    def update(self, file: str):
        # TODO: update the borrower on the json file that match the email of the current borrower.
        with open("./borrowers/candidates.json") as f:
            data = json.load(f)
        for dec in data['candidates']:
            if dec["email"] == self.email:
                dec["age"] = self.age
                dec["income"] = self.income

        with open("./borrowers/candidates.json", 'w') as f:
            f.write(json.dumps(data, indent=4)
