import scipy.stats, numpy, numpy.random
import matplotlib.pyplot as plt
import matplotlib.patches as pt
a=numpy.linspace(0,5,20)
b=a+3*numpy.random.rand(len(a))

#obrigatorio colocar todas as 5 variaveis
# 1 - coeficiente angular
# 2 - coeficiente linear
# 3 - coeficiente de correlacao
# 4 - pvalue
# 5 - erro do coeficiente angular

cf_ang,cf_lin,cf_corr,pvalue, err=scipy.stats.linregress(a,b)

plt.plot(a,b,'ro',a,cf_ang*a+cf_lin,'b-')

plt.show()
