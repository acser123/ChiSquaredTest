import random as rand
import numpy as numpy
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats
from scipy.stats import uniform
from scipy.stats.distributions import chi2
import os

### Set parameters
# Number of random numbers to generate
N = 10000

# number of bins (intervals) to put random numbers into
B = 10

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


CHI = 0

i = 0
while i < len(count):
   # print ("count[i]=", (count[i]))
   CHI = (count[i]-EYi) ** 2 + CHI

   i = i+1

CHI = CHI / EYi

print ("EYi=", EYi)
print ("CHI=", CHI)
print ("Chi-Squared 1-p=", 1-chi2.cdf(CHI, B-1))

i = 0 
t_exp=[]
while i < len(count):
   t_exp.append(N/B)
   i = i +1
# print (t_exp)

# print(scipy.stats.chisquare([16, 18, 16, 14, 12, 12], f_exp=[16, 16, 16, 16, 16, 8]))
print( "scipy.stats.chisquare: ", scipy.stats.chisquare(count, f_exp=t_exp, ddof=B-1))


# print("kstest chi2:",stats.kstest(s, stats.chi2(B-1).cdf))
print("kstest uniform:",stats.kstest(s, stats.uniform.cdf))
# print("kstest norm: ",stats.kstest(s, stats.norm.cdf))
#plt.plot(bins, numpy.ones_like(bins), linewidth=2, color='r')
#plt.show()

