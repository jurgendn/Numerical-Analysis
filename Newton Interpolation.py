import matplotlib.pyplot as plt
import numpy as np


X = [13, 14, 18, 19, 21]
Y = [2210, 2758, 5850, 6878, 9282]


def check(X, Y):
    verify = True
    if (len(X) != len(Y)):
        verify = False
    return verify


# Newton moc bat ki
def newtonInterpolate(X, Y):
    # Create Matrix A:
    A = np.zeros(shape=(len(X), len(Y)))
    for i in range(len(A)):
        for j in range(len(A[0])):
            if j == 0:
                A[i][j] = Y[i]
            else:
                A[i][j] = 0
    # Calc
    for j in range(0, len(A)-1):
        for i in range(0, len(A)-j-1):
            A[i][j+1] = (A[i+1][j]-A[i][j])/(X[i+j+1]-X[i])
    return A


if check(X, Y) == False:
    print("Failure")
else:
    print(newtonInterpolate(X, Y))
    plt.scatter(X, Y)
    plt.plot(X, Y, "-")
    plt.show()
