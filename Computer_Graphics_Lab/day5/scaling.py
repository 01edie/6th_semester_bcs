# SCALING
import matplotlib.pyplot as plt
a = [2, 6, 4, 2]
b = [2, 2, 4, 2]
c = []
d = []


def new_points(x, y, sx, sy):
    T = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
    T1 = [[x], [y], [1]]
    R = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(T)):

        # iterating by column by B
        for j in range(len(T1[0])):

            # iterating by rows of B
            for k in range(len(T1)):
                R[i][j] += T[i][k] * T1[k][j]

    c.append(R[0][0])
    d.append(R[1][0])


# new_points(3,5,2,2)
# print(c,d)
for i in range(4):
    new_points(a[i], b[i], 3, 4)

print(a, b)
plt.plot(a, b)
plt.show()

print(c, d)
plt.plot(c, d)
plt.show()
