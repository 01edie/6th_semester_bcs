# TRANSLATION by value, not by using matrix multiplication
import matplotlib.pyplot as plt
a = [2, 6, 4, 2]
b = [2, 2, 4, 2]
c = []
d = []


# plt.plot(a,b)
# plt.show()

tx = 3
ty = 5

for i in a:
    c.append(i+tx)

for j in b:
    d.append(j + ty)

print(a, b)
plt.plot(a, b)
plt.pause(1)
print(c, d)
plt.plot(c, d)
plt.show()
