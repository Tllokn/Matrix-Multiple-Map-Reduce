import sys
import numpy as np

if __name__ == '__main__':
    i = sys.argv[1]
    sizeA = (int(i), int(i))
    sizeB = (int(i), int(i))

    wA = np.random.randint(5, size=sizeA)
    wB = np.random.randint(7, size=sizeB)
    res = np.matmul(wA,wB)

    f = open("tmp/MA.txt", "w")

    for i in range(wA.shape[0]):
        for j in range(wA.shape[1]):
            f.write(f"{i} {j} {wA[i][j]}\n")

    f.close()

    f = open("tmp/MB.txt", "w")
    for i in range(wB.shape[0]):
        for j in range(wB.shape[1]):
            f.write(f"{i} {j} {wB[i][j]}\n")

    f.close()

    f = open("tmp/answer.txt", "w")
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            f.write(f"{i} {j} {res[i][j]}\n")

    f.close()


