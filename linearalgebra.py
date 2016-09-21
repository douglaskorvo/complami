import numpy as np

#produto escalar
#print a.dot(b)

a=np.array([0,1,2,3,4,5]).reshape(2,3)
b=np.array([1,1,2,3,4,5,6,7,8]).reshape(3,3)

print a
print b

print

print a.shape,b.shape

print

print a.dot(b), a.dot(b).shape

print "TRANSPOSTA"
print a.T
print
print "TRANSPOR VETOR"
#para transpor um vetor eh necessario coloca-lo #dentro de outro vetor
v=np.array([[1,2,3,4]])
print v.T
print 
print "INVERSAO MATRICIAL"
print np.linalg.inv(b)
print
print "DETERMINANTE DA MATRIZ"
print np.linalg.det(b)
