import numpy as numpy
import matplotlib.pyplot as plt
from scipy.stats.distributions import chi2


### Set parameters
# Number of random numbers to generate
N = 1000000

# number of bins (intervals) to put random numbers into
B = 100

# range
range = 1

# width of a bin
W = range / B

# Expected value EYi
EYi = N / B

print("N=",N)
print("B=",B)
print("W=",W)
s = numpy.random.uniform(0,1,N)

count, bins, ignored = plt.hist(s, B, density=True)

# print ("s=", s)
print ("count=",count)
# print ("bins=",bins)

#plt.plot(bins, numpy.ones_like(bins), linewidth=2, color='r')
#plt.show()

CHI = 0
i = 0
while i < len(count):
   CHI = (count[i]*B-B) ** 2 + CHI
   i = i+1

CHI = CHI / EYi

print ("CHI=", CHI)
print ("1-p=", 1-chi2.cdf(CHI, B-1))