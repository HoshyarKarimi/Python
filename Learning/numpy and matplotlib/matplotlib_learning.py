from matplotlib import pyplot as plt
import numpy as np

# xs = np.arange(0, 5)
# y1 = np.arange(1, 6)
# y2 = [2**i for i in range(5)]
# plt.plot(xs, y1, "g-o", xs, y2, "b-^")
# plt.show()

# data = np.arange(1, 21).reshape(5, 4)
# print(data)
# plt.plot(data)
# plt.show()
# plt.plot(data.transpose())
# print(data.transpose())
# plt.show()

days = np.arange(0, 21)
other_site = np.arange(0, 21)
real_python = other_site ** 2

plt.plot(days, other_site)
plt.plot(days, real_python)
plt.xticks([0, 5, 10, 15, 20])
plt.show()
