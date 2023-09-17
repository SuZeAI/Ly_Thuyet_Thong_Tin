# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN02:
# solution
import numpy as np
DMC = {
    'codename': 'C',
    'codewords': ['1', '01', '001', '000']
}
# lesson 1
def evenly(codeword) -> bool:
    return True if len(set([len(i) for i in codeword])) == 1 else False
def degenerate(codeword) -> bool:
    return False if len(set(codeword)) == len(codeword) else True
def decode_unique(codeword) -> bool:
    ls = codeword.copy()
    for i in range(len(codeword)):
        for j in range(i + 1, len(codeword)):
            tmp = "".join(ls[i : (j + 1)])
            ls.append(tmp)
    return False if degenerate(ls) else True
def prefix(codeword) -> bool:
    for i in codeword:
        for j in codeword:
            if i != j:
                i: str = i.replace(j, "S")
                if i[0] == "S": return False
    return True

# lesson 2
def codezeros(codeword) -> bool:
    for i in codeword:
        if "1" not in i: return True
    return False
def sum2code(code1, code2) -> str:
    while len(code1) < len(code2):
        code1 = "0" + code1
    while len(code1) > len(code2):
        code2 = "0" + code2
    arr1 = np.array(list(map(int, list(code1))))
    arr2 = np.array(list(map(int, list(code2))))
    return "".join(map(str, (arr1 + arr2) % 2))
def linear_block_code(codeword) -> bool:
    length = len(set(codeword))
    ls = codeword.copy()
    if not codezeros(codeword): return False
    for i in range(len(codeword) - 1):
        for j in range(i + 1, len(codeword)):
            tmp: str = sum2code(codeword[i],codeword[j])
            ls.append(tmp)
            if len(set(ls)) != length: return False
    return True
# lesson 3
def base_system(codeword) -> bool:
    length = len(set(codeword))
    ls = codeword.copy()
    for i in range(len(codeword) - 1):
        for j in range(i + 1, len(codeword)):
            tmp: str = sum2code(codeword[i],codeword[j])
            ls.append(tmp)
            if len(set(ls)) != length: return False
    return True
# lesson 4
def right_shift(code) -> str:
    return code[1:] + code[0]
def linear_code_circle(codeword) -> bool:
    ls = codeword.copy()
    length = len(codeword)
    for i in codeword:
        tmp =  i
        for j in range(len(i)):
            tmp = right_shift(tmp)
            ls.append(tmp)
            if len(set(ls)) != length: return False
    return True
# lesson 5
def checkcodeset(codeset1, codeset2) -> bool:
    return True if sorted(codeset1) == sorted(codeset2) else False

