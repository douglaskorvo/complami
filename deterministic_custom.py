import scipy.stats, numpy, math, sys
import matplotlib.pyplot as plt

class deterministic_gen(scipy.stats.rv_continuous):
        def _pdf(self,x):
                return (1.0/(2*math.sqrt(3.1415)))*(math.exp(-(x-3)**2)+math.exp(-x**2))

mydist=deterministic_gen(name='custom')

y=mydist.rvs(size=1000)

plt.plot(y,'bo')
plt.show()
