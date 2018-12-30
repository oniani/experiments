"""
This is interesting
Recheck it
"""


import sys
import numpy as np
import matplotlib.pyplot as plt


size = lambda x: sys.getsizeof(x)

list_plot_cords = []
ndarray_plot_cords = []

for i in range(10000):
    list_plot_cords.append(size(list(range(i))))
    ndarray_plot_cords.append(size(np.arange(i)))

plt.title("Python 'list' VS NumPy 'ndarray'")

plt.xlabel("'list' space usage", color="blue", fontsize="12")
plt.ylabel("'ndarray' space usage", color="blue", fontsize="12")

plt.plot(list_plot_cords,    ndarray_plot_cords, c='orange', label="list VS ndarray")
plt.plot(list(range(10000)), list_plot_cords,    c='red'   , label="list performance")
plt.plot(list(range(10000)), ndarray_plot_cords, c='green' , label="ndarray performance")

plt.legend(loc="best")
plt.show()

# ANNOTATION ~ READ THIS
# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111)

# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = ax.plot(t, s, lw=2)

# ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )

# ax.set_ylim(-2,2)
# plt.show()
