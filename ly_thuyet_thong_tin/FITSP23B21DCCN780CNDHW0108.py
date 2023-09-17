# Vũ Thành Tuyên
# B21DCCN780
# D21CQCN12-B
# G06
# BN08:
# solution
import numpy as np
import matplotlib.pyplot as plt
DMC = {
    "x": ["x1", "x2", "x3"],
    "p": [0.2, 0.3, 0.5]
}
# lesson 1

def entropy(P: list) -> float:
    resulft = 0.0
    for i in P:
        if i != 0:
            resulft -= i * np.log2(i)
    return round(resulft, 5)

print(entropy(DMC['p']))

# lesson 2
def entropy_3d() -> None:
    p = np.round(np.random.random(100) / 2, 1)
    q = np.round(np.random.random(100) / 2, 1)
    r = 1 - p - q
    ep_ls = []
    for a in zip(p, q, r):
        ep_ls.append(entropy(a))
    ep_ls = np.array(ep_ls)

    fix = plt.figure()
    ax = fix.add_subplot(111, projection="3d")
    for item in zip(q, p, ep_ls):
        ax.scatter(item[0], item[1], item[2],color="b", s=3)

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 5])

    ax.set_title("3D entropy with p, q")
    ax.set_xlabel('q')
    ax.set_ylabel('p')
    ax.set_zlabel('entropy')
    plt.show()

entropy_3d()

#lesson 3

def p0(r) -> None:
    rs_enntr = []
    for i in r:
        r_tmp = np.array([i]*100)
        p = np.round(np.random.random(100) * (1 - i), 1)
        q = 1 - i - p
        ent = []
        for item in zip(q, p, r_tmp):
            ent.append(entropy(item))
        rs_enntr.append(np.max(ent))
    print(len(r))
    print(len(rs_enntr))
    plt.scatter(r, np.array(rs_enntr), color="b")
    plt.xlim((0, 1))
    plt.ylim((0, 5))
    plt.title("Hp0_max and p0")
    plt.xlabel("p0")
    plt.ylabel("Hp0_max")
    plt.show()


p0(np.round(np.random.random(100) / 2, 1))



