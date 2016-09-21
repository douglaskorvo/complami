import scipy.stats as st
import matplotlib.pyplot as plt
import numpy
rv=st.norm()

d = rv.rvs(size=1000)

#funcao de densidade de probabilidade
#no ponto 'x' que for selecionado
#no exemplo x=0

print rv.pdf(0)

x=numpy.linspace(-3,3,100)
y=rv.pdf(x)

#funcao de probabilidade cumulativa

print rv.cdf(0)
print
print rv.mean()

plt.plot(x,y,'ro')
plt.show()
