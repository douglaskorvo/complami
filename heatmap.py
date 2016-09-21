import numpy as np
import matplotlib.pyplot as plt
plt.style.use(u'fivethirtyeight')

def f(x,y):
        return (1 + np.cos(x*x+y))

size_square=1000

x_front=[-5,5]
y_front=[-5,5]

x=np.linspace(x_front[0],x_front[1],size_square)
y=np.linspace(y_front[0],y_front[1],size_square)

z=np.zeros((size_square,size_square))

for i in range(size_square):
        for j in range(size_square):
                z[i][j]=f(x[i],y[j])

extent=[x.min(),x.max(),y.min(),y.max()]

extent1=[x.max(),x.min(),y.max(),y.min()]

plt.clf()
plt.imshow(z,extent=extent, interpolation='none',cmap='hot')
plt.show()




