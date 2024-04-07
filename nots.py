# import sys
# print(sys.argv[1:])
import random

# import subprocess
#
# subprocess.call(["python", "htmls.py"])

# import requests
# #
# # r = requests.get("https://stepik.org/lesson/3378/step/1?unit=961", params={"var":"var", "sss":"sss"})
# # print(r.url)
# #
# # r = requests.get("https://stepik.org/lesson/3378/step/1?unit=961", cookies={"Coc":"coo"})
# # print(r.text)
# # print(r.cookies)
#
# url = r"https://stepik.org/media/attachments/course67/3.6.3/"
#
# r = requests.get(r"https://stepik.org/media/attachments/course67/3.6.3/699991.txt")
#
# t = r.text.split()
#
#
# while r.text[:2] != "We":
#     r = requests.get(r"https://stepik.org/media/attachments/course67/3.6.3/" + r.text)
#     print(r.text)
# print(r.text)


# lst = []
#
# with open("dataset_3380_5.txt", "r", encoding="utf-8") as f:
#     for i in f:
#          r = i.strip()
#          while r.count("  ") != 0:
#              r = r.replace("  ", " ")
#          lst.append(r.split())
#
# dic = {}
# for i in range(1,12):
#     dic[i] = [0,0]
#
# for i in lst:
#     dic[int(i[0])][0] += int(i[2])
#     dic[int(i[0])][1] += 1
#
# for k, v in dic.items():
#     print(k, (v[0] / v[1]) if v[0] != 0 else "-")

from numpy import *

# a = array([[1,2,3], [1,2,3]])
# print(a, a.ndim,a.shape, a.size)

# a = zeros((3,3))
# a[1][2] = 2
# print(a)

# a = arange(1,5)
# print(a)

# a = linspace(1,2, 6)
# print(a)

# a = arange(1,13).reshape((4,3))
# print(a)

from pylab import *
# x = linspace(0, 5, 10)
# y = log2(x)
# print(x)
# print(y)
#
# figure()
# plot(x, y, "r")
# xlabel("X - метка")
# ylabel("Y - метка")
# title("Ну это график")
# show()

# x = linspace(0, 5, 10)
# y = x ** 2
#
# fig = plt.figure()
#
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#
# axes.plot(x, y, "r")
# axes.set_xlabel("x")
# axes.set_ylabel("x")
# axes.set_title("XY")
# show()

x = linspace(0, 5, 10)
y = x ** 2

# fig = plt.figure()
#
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes1 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
#
# axes.plot(x, y, "r")
# axes.set_xlabel("x")
# axes.set_ylabel("y")
# axes.set_title("XY")
#
# axes1.plot(y,x, "g")
# axes1.set_xlabel("y")
# axes1.set_ylabel("x")
# axes1.set_title("XY - 2")
# show()

# fig, axes = plt.subplots(nrows=1, ncols=2)
# for ax in axes:
#     ax.plot(x, y, "g")
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     ax.set_title("XY")
# fig.tight_layout()
# show()


# fig, axes = plt.subplots(figsize=(12,3))
# axes.plot(x, y, "g")
# axes.set_xlabel("x")
# axes.set_ylabel("y")
# axes.set_title("XY")
#
# show()

# fig, axes = plt.subplots()
#
#
# axes.plot(x, x**2, label="Тонко")
# axes.plot(x, x**3, label="Очень тонко")
#
# axes.legend(loc=2)
# axes.set_xlabel("x")
# axes.set_ylabel("y")
# axes.set_title("XY")
#
# show()

from numpy import *
n = random.randn(100000)
fig, axes = plt.subplots(1,2,figsize=(12,4))

axes[0].hist(n)
axes[0].set_xlim((min(n), max(n)))
axes[0].set_title("XY")

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_xlim((min(n), max(n)))
axes[1].set_title("XY")
show()
