from typing import Optional

from fintools import Amortization


class Main:

    @staticmethod
    def annuity(amount: float, rate: float, n: int):
        a = Amortization(amount=amount, rate=rate, n=n)
        return round(a.annuity, 2)

    @staticmethod
    def table(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        a = Amortization(amount=amount, rate=rate, n=n)
        print(a.get_table())
        a.get_table(save_file=save_file)

    @staticmethod
    def plot(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        a = Amortization(amount=amount, rate=rate, n=n)
        graph = a.plot(save_file=save_file)
        return graph
