from matplotlib import pyplot as plt
import numpy as np
from numpy import random

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

# days = np.arange(0, 21)
# other_site = np.arange(0, 21)
# real_python = other_site ** 2

# plt.plot(days, other_site)
# plt.plot(days, real_python)
# plt.xticks([0, 5, 10, 15, 20])
# plt.xlabel("Days of Reading")
# plt.ylabel("Amount of Python Learned")
# plt.title("Python Learned Reading Real Python vs Other Site")
# plt.legend(["Other Site", "Real Python"], loc="best")
# plt.show()

# xs = np.arange(1, 6)
# tops = np.arange(2, 11, 2)
# plt.bar(xs, tops)
# plt.show()

# fruits = {
#     "apples": 5,
#     "oranges": 10,
#     "cucumbers": 3,
#     "pears": 9,
# }
# plt.bar(fruits.keys(), fruits.values())
# plt.show()
# date = [2, 12, 13, 14, 17, 19, 19, 20, 21, 25, 27, 28, 31]
# j = [7, 6, 5, 15, 9, 19, 15, 11, 13, 10, 8, 8, 9]
# plt.plot(date, j, "r")
# plt.title("At-1")
# plt.yticks([i for i in range(0, 21, 5)])
# plt.show()

plt.hist(random.randn(10000), 20)
plt.savefig('/home/hoshyar/bar.png')
