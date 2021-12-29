import numpy as np
from sympy import simplify
from sympy.abc import x


def nhap_mocnoisuy_giatri_tuongung():
    n = int(input("Moi ban nhap vao so moc noi suy: "))
    # Nhap vao cac moc noi suy va gia tri tuong ung
    moc = []
    giatri = []
    for i in range(n):
        print("Moi ban nhap vao moc noi suy thu", i + 1, end=' ')
        a = int(input())
        print("Moi nhap gia tri tuong ung voi moc noi suy thu", i + 1, end=' ')
        b = int(input())
        moc.append(a)
        giatri.append(b)
    return (n, moc, giatri)


def lap_bangtihieu(n, moc, giatri):
    BTH = np.zeros((n, n))
    for i in range(n):
        BTH[i][0] = giatri[i]
    for j in range(1, n):
        for i in range(0, n - j):
            BTH[i][j] = (BTH[i + 1][j - 1] - BTH[i][j - 1]) / (moc[i + j] -
                                                               moc[i])
    return BTH


def in_dathuc_noisuyNewton(n, BTH, moc):
    print('P(x)=', end='')
    print(BTH[0][0], end='')
    trunggian = 0
    for i in range(1, n):
        trunggian = trunggian + 1
        print('+{0}'.format(BTH[0][i]), end='')
        for j in range(0, trunggian):
            print("*(x-{0})".format(moc[j]), end='')


def rutgon_dathuc(n, filetxt, giatri, moc):
    BTH = np.empty((n, n)).tolist()
    for i in range(n):
        BTH[i][0] = giatri[i]
    for j in range(1, n):
        for i in range(0, n - 1 - j):
            BTH[i][j] = (BTH[i + 1][j - 1] - BTH[i][j - 1]) / (moc[i + j] -
                                                               moc[i])
    d = open("rutgon.txt", "w")
    A = BTH[0]
    for i in range(n):
        A[i] = str(A[i])
    d = open("rutgon.txt", "w")
    d.write(A[0])
    trunggian = 0
    for i in range(1, n):
        trunggian = trunggian + 1
        d.write('+{0}'.format(A[i]))
        for j in range(0, trunggian):
            d.write("*(x-{0})".format(moc[j]))
    d = open("rutgon.txt", "r")
    a = d.read()
    print("Rut gon da thuc noi suy Newton ta duoc da thuc:")
    print('P(x)=', end='')
    print(simplify(a))


def P(x, n, BTH, moc):
    P = BTH[0][0]
    trunggian = 1
    for i in range(n - 1):
        trunggian = trunggian * (x - moc[i])
        P += trunggian * BTH[0][i + 1]
    return P
