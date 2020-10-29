import json

from fintools import CashFlow


class Main:

    def __init__(self, amount: float, t: int):
        self.amount = amount
        self.t = t

    @staticmethod
    def present_value(amount: float, rate: float, n: int):
        return CashFlow(amount=self.amount * (1+r) ** (-self.t), t=0)

    @staticmethod
    def future_value(amount: float, rate: float, n: int):
        return CashFlow(amount=self.amount * (1 + r) ** (self.t), t=t)
