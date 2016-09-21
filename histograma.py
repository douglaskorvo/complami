import numpy
data=numpy.arange(10)
datahist,bins = numpy.histogram(data,bins=10)
print datahist
print bins

datahist1,bins1 = numpy.histogram(data,bins=[0,1,2,3,4])

print datahist1
print bins1
