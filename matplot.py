import matplotlib.pyplot as plt
import numpy
import scipy.interpolate as intp


"plt.hist([1,1,1,2,1,1,3,4,5],bins=3)
"plt.show()

x1=[0,1,2,3,4]
x2=[1,-2,3,-4,5]

f_interp_linear = intp.interp1d(x1,y1)
x2=numpy.linspace(0,4,100)

f_interp_cubic = scipy.interpolate.interp1d(x1,y1,kind='cubic')

plt.plot(x1,y1,'o',x2,f_interp_linear(x2), 'g--',x2,f_interp_cubic(x2),'r--')
plt.sho
