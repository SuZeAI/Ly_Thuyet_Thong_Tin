# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN04:
# solution

import numpy as np
H = np.array([[1,0,1,1,1,0,0],[0,1,0,1,1,1,0],[0,0,1,0,1,1,1]])


# lesson 1
def gen(i, n, k, ls, ans) -> None:
    for j in range(ls[i - 1] + 1, n - k + i + 1):
        ls.append(j)
        if i == k:
            tmp = ls.copy()
            tmp.pop(0)
            ans.append(tmp)
        else: gen(i + 1, n, k, ls, ans)
        ls.pop()
def sum2cols(col1, col2) -> np.array:
    return (col1 + col2) % 2

def dmin_H(H: np.array) -> int:
    rows, cols = H.shape
    for i in range(2, cols + 1):
        ans = []
        gen(1, cols, i, [0], ans)
        for item in ans:
            out = np.array([0] * rows)
            for key in item:
                out = sum2cols(out, H[:, key - 1])
            if np.sum(out) == 0: return i
    return -1
print(dmin_H(H))
# lesson 2
def validcode(c, H) -> bool:
    c = np.array(c)
    if len(c) != H.shape[1]: return False
    return True if np.sum((c.dot(H.T))%2) == 0 else False
print(validcode([1, 0, 1, 1, 0], H))
#lesson 3
def genbinary(i, n, ls=[], ans=None):
    for j in range(2):
        ls.append(j)
        if i == n:
            ans.append(ls.copy())
        else: genbinary(i + 1, n, ls, ans)
        ls.pop()
def catalog_words(H) -> list:
    ans = []
    cols = H.shape[1]
    genbinary(1, cols, ans=ans)
    all_codewords = []
    for j in ans:
        if validcode(j, H): all_codewords.append(j)
    return all_codewords
print(catalog_words(H))
# lesson 4
def dmin_define(H: np.array) -> int:
    code_words = np.array(catalog_words(H))
    mn = int(1e9)
    m, n = code_words.shape
    for i in range(m - 1):
        for j in range(i + 1, m):
            sm = [np.abs(code_words[i, key] - code_words[j, key]) for key in range(n)]
            mn = min(mn, np.sum(sm))
    return mn
print(dmin_define(H))
# lesson 5
def dmin_code_linear(H) -> int:
    all_words = catalog_words(H)
    mn = int(1e9)
    for code_words in all_words:
        if sum(code_words) != 0:
            mn = min(sum(code_words), mn)
    return mn
print(dmin_code_linear(H))
print(dmin_H(H))
print(dmin_define(H))
