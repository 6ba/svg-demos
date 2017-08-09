import pandas as pd
import numpy as np
# y = 10+-sqrt(100-(10-x)^2)

x1 = [0.5*x for x in range(400)]

y1 = []
y2 = []

r = 100.0

for x in x1:
    y1.append(r+np.sqrt(r*r-(r-x)*(r-x)))
    y2.append(r-np.sqrt(r*r-(r-x)*(r-x)))


y2.reverse()
x2 = x1.copy()
x2.reverse()

x1.extend(x2)
y1.extend(y2)

print(x1)
print(y1)

def test(x1, y1):
    import matplotlib
    import matplotlib.pyplot as plt
    # basic
    f1 = plt.figure(1)
    plt.subplot(211)
    plt.scatter(x1, y1)
    plt.show()

test(x1, y1)

