import json

from fintools import CashFlow


class Main:

    @staticmethod
    def present_value(amount: float, rate: float, n: int):
            t = CashFlow(amount, n)
            pv = t.pv(r=rate)
            pv = pv.to_dict()
            return json.dumps(pv, indent=4)

    @staticmethod
    def future_value(amount: float, rate: float, n: int):
            fv = amount * ((1 + rate) ** n)
            t = CashFlow(fv, n)
            fv = t.to_dict()
            return json.dumps(fv, indent=4)
