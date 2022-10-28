import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import uniform
from scipy.stats.distributions import chi2
import math as m


### Set parameters
# Number of random numbers to generate
N = 1000000

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

# s = np.random.uniform(0,1,N)
# s = np.random.normal(0,1,N)
rng = np.random.default_rng()
s = stats.uniform.rvs(size=N, random_state=rng)

count, bins, ignored = plt.hist(s, B, density=False)

### Build Chi-Squared statistics
CHI = 0

i = 0
while i < len(count):
   CHI = (count[i]-EYi) ** 2 + CHI
   i = i+1

CHI = CHI / EYi

print ("EYi=", EYi)
print ("CHI=", CHI)

print ("Chi-Squared 1-p=", 1-chi2.cdf(CHI, B-1))

### Build expected frequencies list
i = 0 
t_exp=[]
while i < len(count):
   t_exp.append(N/B)
   i = i +1

print( "scipy.stats.chisquare: ", stats.chisquare(count, f_exp=t_exp))

print("kstest uniform:",stats.kstest(s, stats.uniform.cdf))
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()




