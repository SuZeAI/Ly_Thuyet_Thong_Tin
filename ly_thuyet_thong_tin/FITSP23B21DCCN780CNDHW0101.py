# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN01:
# solution

# import package
import pandas as pd
import numpy as np
class Node(object):
    def __init__(self, data= None, value= None, leaf= None, IG= None, text = None, type=None):
        self.data = [data]
        self.val = [value]
        self.IG = [IG]
        self.text = [text]
        self.type = [type]

class TreeClasscisition(object):
    def __init__(self):
        self.root = None

    def fit(self, data: pd.DataFrame):
        self.root = [[Node(data=data)]]
        self.data = data
        self.list_decision = data.columns
        self.depth = len(data.columns)
        self.buildtree()

    def union(self, data, text) -> list[str]:
        return data[text].unique()

    def divide_data(self, data, text) -> list:
        ls_dt = []
        uni = self.union(data, text)
        for item in uni:
            dt = data.iloc[data[text].values == item]
            ls_dt.append((dt,item))
        return ls_dt

    def buildtree(self):
        for i in range(1, self.depth + 1):
            ls = []
            nd = self.root[i - 1]
            for node in nd:
                node.text[0] = self.list_decision[i - 1]
                if node.data[0] is not None:
                    node.IG[0] = self.information_gain(node.data[0], node.text[0])
                if node.data[0] is not None:
                    if len(self.union(node.data[0], "solution")) > 1:
                        for key, text in self.divide_data(node.data[0], node.text[0]):
                            ls.append(Node(data=key, type=text))
                    elif node.val[0] is None :
                        ls.append(Node(value=self.union(node.data[0], "solution")[0], IG=node.IG[0]))
                    else:
                        ls.append(Node(value=node.val[0], IG=node.IG[0]))
            self.root.append(ls)
    def print_tree(self):
        for i in self.root:
            for key in i:
                print(f"val: {key.val}, type: {key.type}, IG: {key.IG} |||| ", end="")
            print()
    def information_gain(self, data: pd.DataFrame, text: str) -> float:
        uni = data[text].unique()
        nb = len(data[text])
        IG = self.entropy(data)
        for item in uni:
            ntmp = len(data[text][data[text].values == item])
            sl = np.array(data["solution"][data[text].values == item])
            dt = pd.DataFrame(data={
                "solution": sl
            })
            IG -= (ntmp/nb) * self.entropy(dt)
        return np.round(IG, 5)


    def entropy(self, data: pd.DataFrame) -> float:
        fre_A_B = len(np.array(data["solution"].values))
        fre_A = len(np.array(data["solution"][data["solution"].values == 1]))
        fre_B = len(np.array(data["solution"][data["solution"].values == 2]))
        fre_A = fre_A_B if fre_A == 0 else fre_A
        fre_B = fre_A_B if fre_B == 0 else fre_B
        etr = -1 * (fre_A/fre_A_B) * np.log2(fre_A/fre_A_B) - (fre_B/fre_A_B) * np.log2(fre_B/fre_A_B)
        return np.round(etr, 5)


def main():
    data = pd.read_csv("benhnhan.csv")
    for i in data.columns:
        for idx, val in enumerate(data[i].unique(), 1):
            data[i] = data[i].replace({val: idx})
    ob = TreeClasscisition()
    ob.fit(data)
    ob.print_tree()
main()

