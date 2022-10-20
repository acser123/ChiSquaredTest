import random as rand
import numpy as numpy
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import uniform
from scipy.stats.distributions import chi2
import os

### Set parameters
# Number of random numbers to generate
N = 10000000

# number of bins (intervals) to put random numbers into
B = 100

# range
range = 1

# width of a bin
W = range / B

# Expected value EYi
EYi = N/B

print("N=",N)
print("B=",B)
print("W=",W)

# s = numpy.random.uniform(0,1,N)
# s = rand.random()
# s = numpy.random.normal(0,1,N)
rng = np.random.default_rng()
s = stats.uniform.rvs(size=N, random_state=rng)

count, bins, ignored = plt.hist(s, B, density=False)

# print ("s=", s)
print ("count=",count)
# print ("bins=",bins)

#plt.plot(bins, numpy.ones_like(bins), linewidth=2, color='r')
#plt.show()

CHI = 0
CHIYates = 0
i = 0
while i < len(count):
   # print ("count[i]=", (count[i]))
   CHI = (count[i]-EYi) ** 2 + CHI
   CHIYates = (abs(count[i]-EYi)-0.5) ** 2 + CHIYates
   i = i+1

CHI = CHI / EYi
CHIYates = CHIYates / EYi
print ("EYi=", EYi)
print ("CHI=", CHI)
print ("Chi-Squared 1-p=", 1-chi2.cdf(CHI, B-1))
print ("Chi-Squared Yates correction 1-p=", 1-chi2.cdf(CHIYates, B-1))


print("kstest chi2:",stats.kstest(s, stats.chi2(B-1).cdf))
print("kstest uniform:",stats.kstest(s, stats.uniform.cdf))
print("kstest norm: ",stats.kstest(s, stats.norm.cdf))