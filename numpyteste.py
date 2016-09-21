import numpy
array = numpy.arange(10,22,2)
print
print array

array.shape
print
print array.reshape(2,3)

print
a=[0,1,2,3,4,5]
b=numpy.array(a).reshape(3,2)
print b

print "ACESSANDO ELEMENTOS NO ARRAY"
print b[0,1]

for elemento in b:
        print elemento

a=numpy.array([[0,1],[2,3],[3,4],[4,5],[5,6]])
print a
print
print a.max()
print a.min()
print a.argmax()
print a.argmin()

print
b = a.max(axis=0)
print b.max()
print a.max(axis=1)
print a.ptp(axis=1)
print a.clip(2,5)
a=numpy.arange(9).reshape(3,3)
print a
print a.trace()


