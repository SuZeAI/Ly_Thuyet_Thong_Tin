# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN07:
# solution

import numpy as np
code_cl = {
    'codename': 'C',
    'nL': 7,
    'poly': [0, 1, 2, 4],
    'isGPoly': 0
}
def convert_to_H(poly, nl) -> np.array:
    ls = []
    deg_H = max(poly)
    for i in range(nl):
        if i in poly:
            ls.append(1)
        else:
            ls.append(0)
    H = [ls]
    for row in range(1, nl - deg_H):
        tmp = [H[row - 1][-1]] + H[row - 1][:-1]
        H.append(tmp)
    return np.array(H)

H = convert_to_H(code_cl["poly"], code_cl['nL'])
def gen_comb(i, n, k, ls=[0], ans=None) -> None:
    for j in range(ls[i - 1] + 1, n - k + i + 1):
        ls.append(j)
        if i == k:
            tmp = ls.copy()
            tmp.pop(0)
            ans.append(tmp)
        else: gen_comb(i + 1, n, k, ls, ans)
        ls.pop()
# lesson 1
def a_sum_check(H: np.array) -> np.array:
    ans = []
    rows, cols = H.shape
    for i in range(1,rows + 1):
        gen_comb(1, rows, i, ans=ans)
    rs = []
    for item in ans:
        tmp = np.array([0]*cols)
        for i in item:
            tmp += H[i - 1]
        rs.append(tmp%2)
    return np.array(rs)
print(a_sum_check(H))
# lesson 2
def sum2cols(col1, col2) -> np.array:
    return (col1 + col2) % 2
def dmin_H(H: np.array) -> int:
    rows, cols = H.shape
    for i in range(2, cols + 1):
        ans = []
        gen_comb(1, cols, i, [0], ans)
        for item in ans:
            out = np.array([0] * rows)
            for key in item:
                out = sum2cols(out, H[:, key - 1])
            if np.sum(out) == 0: return i
    return -1
def full_check_orthogonality(H):
    J = dmin_H(H) - 1
    ans = []
    nl = H.shape[1]
    ls = a_sum_check(H)
    gen_comb(1, ls.shape[0], J, ans=ans)
    for item in ans:
        tmp = np.array([0] * nl)
        for i in item:
            tmp += ls[i - 1]
        if  len([i for i in tmp if i > 1]) == 1: return True
    return False
print(full_check_orthogonality(H))
# lesson 3
def set_check_orthogonality(H):
    J = dmin_H(H) - 1
    ans = []
    nl = H.shape[1]
    ls = a_sum_check(H)
    check = [False] * nl
    gen_comb(1, ls.shape[0], J, ans=ans)
    for item in ans:
        tmp = np.array([0] * nl)
        for i in item:
            tmp += ls[i - 1]
        if len([i for i in range(len(tmp)) if tmp[i] > 1]) == 1:
            tmp1 = [i for i in tmp if i > 1]
            check[tmp[0]] = True
    return True if (len(set(check)) == 1 and (True in check)) else False

print(set_check_orthogonality(H))



