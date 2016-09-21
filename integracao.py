import scipy.integrate as int
import math
import matplotlib.pyplot as plt
from numpy import inf

def f(x):
        return x*x
x=list()
y=list()
y2=list()

for i in range(0,100):
        x.append(i)
        y.append(f(i))
        y2.append(int.integrate.quad(f(i),0,i)


plt.plot([x],[y])
plt.show()


