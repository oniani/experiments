import math
import matplotlib.pyplot as plt


plt.plot(
    list(range(10000)),
    list(map(math.sqrt, list(range(10000)))),
    label="f (x) = √x",
)
plt.plot(list(range(10000)), [i for i in range(10000)], label="f (x) = x")
plt.plot(
    list(range(10000)), [i ** 2 for i in range(10000)], label="f (x) = x^2"
)

plt.legend()
plt.show()
