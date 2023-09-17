# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN06:
# solution
from collections import Counter
import numpy as np
# print poly
def print_poly(ans) -> None:
    tmp1 = ""
    for i in ans:
        tmp = "("
        for j in range(len(i)):
            if i[j] == "1":
                if j != len(i) - 1:
                    tmp += f" x^{len(i) - j - 1} + "
                else:
                    tmp += " 1   "
        tmp1 += f"{tmp[:-2]} ) * "
    print(tmp1[:-2])

# GF2
class GF(object):
    def degree_GF2(self, a) -> int:
        return -1 if a == 0 else len(bin(a)[2:]) - 1

    def GF2_mul(self, a, b) -> int:
        assert a >= 0 and b >= 0
        resluft = 0
        while a != 0:
            if a & 1 == 1:
                resluft ^= b
            a >>= 1
            b <<= 1
        return resluft

    def GF2_add(self, a, b) -> int:
        assert a >= 0 and b >= 0
        return a ^ b

    def GF2_div_mod(self, a, b) -> tuple:
        assert b != 0
        assert a >= 0
        resulft = 0
        while self.degree_GF2(a) >= self.degree_GF2(b):
            resulft ^= 1 << (self.degree_GF2(a) - self.degree_GF2(b))
            a ^= (b << (self.degree_GF2(a) - self.degree_GF2(b)))
        return resulft, a

    def is_irreducible_poly(self, f) -> bool:
        assert f >= 0
        deg = self.degree_GF2(f)
        if deg == 1: return True
        if deg == 0: return False
        for i in range(2, np.power(2, int(np.sqrt(deg)) + 1)):
            if self.GF2_div_mod(f, i)[1] == 0:
                return False
        return True

    def simplify_pl(self, f) -> list:
        assert f >= 0
        ans = []
        i = 2
        deg = self.degree_GF2(f)
        while i <= np.power(2, int(np.sqrt(deg)) + 1):
            if self.is_irreducible_poly(i):
                while self.GF2_div_mod(f, i)[1] == 0:
                    ans.append(bin(i)[2:])
                    f = self.GF2_div_mod(f, i)[0]
            deg = self.degree_GF2(f)
            i += 1
        if f != 1: ans.append(bin(f)[2: ])
        return ans
    def power_poly(self, f, n) -> int:
        if n == 0: return 1
        if n == 1: return f
        pow = self.power_poly(f, n//2)
        if n & 1:
            return self.GF2_mul(pow, self.GF2_mul(pow, f))
        else: return self.GF2_mul(pow, pow)
gf = GF()

# lesson 1
def list_poly_irreducible(k) -> list:
    assert k >= 0
    ans = []
    for i in range(np.power(2, k), np.power(2, k + 1)):
        if gf.is_irreducible_poly(i): ans.append(bin(i)[2:])
    return ans
print(list_poly_irreducible(7))
# lesson 2
def check_irreducible(k) -> bool:
    return gf.is_irreducible_poly(int(k, 2))
print(check_irreducible("11"))
# lesson 3
def simplify_poly(n) -> list:
    f = np.power(2, n) + 1
    return gf.simplify_pl(f)
print_poly(simplify_poly(7))
# lesson 4
def gen_factor(i, n, ls, ans, tmp=[]) -> None:
    for j in range(ls[i - 1][1] + 1):
        tmp.append(j)
        if i == n:
            ans.append(tmp.copy())
        else:
            gen_factor(i + 1, n, ls, ans, tmp)
        tmp.pop()
def list_factor(n) -> list:
    f = np.power(2, n) + 1
    ans = gf.simplify_pl(f)
    ls = list(Counter(ans).items())
    rs = []
    gen_factor(1, len(ls), ls, rs)
    resulft = []
    for key in rs:
        tmp = 1
        for j in range(len(key)):
           tmp = gf.GF2_mul(gf.power_poly(int(ls[j][0], 2), key[j]), tmp)
        resulft.append(bin(tmp)[2:])
    return resulft
for i in list_factor(3):
    print_poly([i])
