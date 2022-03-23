# CLOCKWISE ROTATION
#for details in clockwise and anticlockwise rotation see the theory 
import matplotlib.pyplot as plt
import math
a = [2, 4, 3, 2]
b = [2, 2, 3, 2]
c = []
d = []


def new_points(x, y, de):
    T = [[math.cos(math.radians(de)), (-math.sin(math.radians(de))), 0],[math.sin(math.radians(de)), math.cos(math.radians(de)), 0], [0, 0, 1]]
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
    new_points(a[i], b[i], 180)

print(a, b)
plt.plot(a, b)
plt.show()
print(c, d)
plt.plot(c, d)
plt.show()
