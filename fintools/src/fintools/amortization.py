from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount: float, rate: float, n: int):
        self.amount = amount
        self.rate = rate
        self.n = n

    @property
    def annuity(self) -> float:
        a = self.amount * self.rate / (1 - (1 + self.rate) ** (-self.n))
        return a

    def get_table(self, save_file: Optional[str] = None) -> pd.DataFrame:
        df = pd.DataFrame(index=range(0, self.n + 1), columns=["t", "B", "A", "P", "I"])
        df["t"] = range(0, self.n + 1)

        df.loc[0, "B"] = self.amount
        df.loc[1:, "A"] = self.annuity

        for j in range(1, self.n + 1):
            df.loc[j, "I"] = df.loc[j - 1, "B"] * self.rate
            df.loc[j, "P"] = df.loc[j, "A"] - df.loc[j, "I"]
            df.loc[j, "B"] = df.loc[j - 1, "B"] - df.loc[j, "P"]
        if save_file:
            df.to_csv(save_file)
        return df

    def plot(self, show: bool = False, save_file: Optional[str] = None) -> None:
        fig, ax = plt.subplots()
        x = self.get_table().t.values
        bars1 = self.get_table().P.values
        bars2 = self.get_table().I.values
        bars1[0] = 0
        bars2[0] = 0
        ax.bar(x, bars1, label="P", color="blue")
        ax.bar(x, bars2, bottom=bars1, label="I", color="orange")
        ax.legend()
        ax.set_title("Amortization Payment")
        ax.set_xlabel("t")
        ax.set_ylabel("$$$")
        ax.grid()
        if save_file:
            plt.savefig(save_file)
        if show:
            plt.show()
