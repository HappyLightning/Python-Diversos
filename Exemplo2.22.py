import numpy
a = numpy.arange(12)
print(a, type(a), "\n")
a.shape = 3, 4
print(a, '\n')
print(a[2], '\n')
print(a[2, 1], '\n')
print(a[:, 1], '\n')
a.transpose()
print(a)
