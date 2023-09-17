# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN05:
# solution
import math
import numpy as np
import matplotlib.pyplot as plt

# Griesmer:
dmin = 3
k = [1, 2, 3, 4, 5, 6, 7]

def griesmer(dmin, k) -> None:
    ans = []
    for i in k:
        tmp = 0.0
        for j in range(i):
            tmp += dmin/(np.power(2, j))
        print(tmp)
        if tmp.is_integer(): ans.append(int(tmp))
        else: ans.append(int(tmp + 1))
    plt.plot(k, ans, "ro-")
    plt.title("griesmer")
    plt.xlabel("k")
    plt.ylabel("l")
    plt.show()

#  Plotkin
L = 7
K = [1, 2, 3, 4, 5, 6, 7, 9]
def  plotkin(L, K):
    ans = []
    for i in K:
        tmp = (L * np.power(2, i - 1))/(np.power(2, i) - 1)
        ans.append(int(tmp))
    plt.plot(K, ans, "bo-")
    plt.title("Plotkin")
    plt.xlabel("K")
    plt.ylabel("dmin")
    plt.show()

# Hamming
LL = 9
T = [1, 2, 3, 4, 5, 6, 7]
def hamming(LL, T):
    ans = []
    for i in T:
        tmp = 0
        for j in range(i + 1):
            tmp += math.comb(LL, j)
        ans.append(int(LL - np.log2(tmp)))
    plt.plot(T, ans, "yo-")
    plt.title("hamming")
    plt.xlabel("T")
    plt.ylabel("K")
    plt.show()
hamming(LL, T)
