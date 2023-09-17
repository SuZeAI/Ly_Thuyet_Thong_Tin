# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN02:
# solution

# Func and Class
import heapq
import numpy
import numpy as np

DMC = {
    'source': 'X',
    'elsym': ['x_1', 'x_2', 'x_3', 'x_4'],
    'elprob': [0.125, 0.25, 0.125, 0.5]
}
def create_dict(ls) -> dict:
    dic = dict()
    for i in ls:
        dic[i] = ""
    return dic
def element(s1, s2) -> tuple:
    tmp = s1[0][0] + " " + s2[0][0]
    sum = s1[0][1] + s2[0][1]
    return (tmp, sum)
def answer(dic, s1, s2) -> None:
    for i in s1[0][0].split():
        dic[i] = "0" + dic[i]
    for i in s2[0][0].split():
        dic[i] = "1" + dic[i]
def reverse_dic(dic) -> dict:
    dic_new = dict()
    for key, value in dic.items():
        dic_new[value] = key
    return dic_new
def entropy(elprob) -> float:
    ans = 0.0
    for i in elprob:
        ans -= i * np.log2(i)
    return ans
class Priority_queue(object):
    def __init__(self, ls=[]):
        self.__ls = ls
    def push(self, tmp) -> None:
        self.__ls = [tmp] + self.__ls
    def get_min(self) -> list:
        return heapq.nsmallest(1, self.__ls, key=lambda x : x[1])
    def remove(self, tmp) -> None:
        self.__ls.remove(tmp[0])
    def length(self) -> int:
        return len(self.__ls)

# lesson 1
def elcodeword(elsym: list, elprob: list):
    sym_prob = list(zip(elsym, elprob))
    dic_x = create_dict(elsym)
    pri_qe = Priority_queue(sym_prob)
    while pri_qe.length() != 1:
        s1 = pri_qe.get_min()
        pri_qe.remove(s1)
        s2 = pri_qe.get_min()
        pri_qe.remove(s2)
        answer(dic_x, s1, s2)
        pri_qe.push(element(s1, s2))
    sr = pri_qe.get_min()
    return dic_x
print(elcodeword(DMC['elsym'], DMC['elprob']))
# lesson 2
def encode() -> str:
    dic_x = elcodeword(DMC['elsym'],DMC['elprob'])
    with open("./FITSP23B21DCCN780CNDHW0102.txt", mode="r") as f:
        a = f.read()
        ans = ""
        tmp = ""
        for i in list(a):
            tmp += i
            if i.isdigit():
                ans += dic_x[tmp]
                tmp=""
        return ans
# print(encode())
# lesson 3
def decode() -> str:
    dic_x = reverse_dic(elcodeword(DMC['elsym'], DMC['elprob']))
    with open(file="./FITSP23B21DCCN780CNDHW0102.txt", mode="r") as f:
        ip = f.read()
        ans = ""
        tmp = ""
        for i in list(ip):
            tmp += i
            if tmp in dic_x.keys():
                ans += dic_x[tmp]
                tmp = ""
        ans += tmp
        return ans
print(decode())
# lesson 4
def avg_l(elword) -> float:
    ls = [len(i) for i in elword]
    return np.average(ls)
def delta(elprob, elword) -> float:
    return entropy(elprob) / avg_l(elword)
def sigma_l_2(elword, elprob) -> float:
    ls = [len(i) for i in elword]
    avg = avg_l(elword)
    ans  = 0.0
    for prob, lth in zip(elprob, ls):
        ans += prob * ((lth - avg)**2)
    return ans
elword = elcodeword(DMC['elsym'], DMC['elprob']).values()
print(avg_l(elword))
print(delta(DMC['elprob'], elword))
print(sigma_l_2(elword, DMC['elprob']))
