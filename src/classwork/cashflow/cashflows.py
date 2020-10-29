from typing import Dict, Optional


class CashFlow:

    def __init__(self, amount: float, n: int):
        self.amount = amount
        self.n = n

    def pv(self, r: float) -> 'CashFlow':
        pv = self.amount / ((1 + r) ** self.n)
        cf = CashFlow(pv, 0)
        return cf

    def shift(self, n: int, r: float) -> 'CashFlow':
        pv = self.amount / ((1 + r) ** self.n)
        fv = pv * ((1 + r) ** n)
        cf = CashFlow(fv, n)
        return cf

    def merge(self, other: 'CashFlow', r: float, reverse: bool = False) -> 'CashFlow':
        if reverse is False:
            b = other.amount / ((1 + r) ** other.n)
            b = b + self.amount
            m = CashFlow(b, self.n)
            return m
        else:
            a = self.amount * ((1 + r) ** other.n)
            a = a + other.amount
            m = CashFlow(a, other.n)
            return m

    def to_dict(self, decimal_places: Optional[int] = 2) -> Dict:
        return {
            "amount": self.amount if decimal_places is None else round(self.amount, decimal_places),
            "n": self.n
        }
