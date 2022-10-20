import random as rand
import scipy as scipy
import numpy as numpy
from scipy.stats.distributions import chi2
import os

### Set parameters
# Number of random numbers to generate
N = 10000

# number of bins (intervals) to put random numbers into
B = 100

# range
range = 1

# width of a bin
W = range / B

print("N=",N)
print("B=",B)
print("W=",W)

### Initialize list of counters of frequencies in bins
A=[]
i = 0
while i<B:
    A.append(0)
    i += 1

### Generate N random numbers
i=1
while i < N+1:
   # R = rand.random()
   # R = rand.uniform (0, 1)
   R = numpy.random.uniform(0, 1)
   # R = rand.normal (0, 1)
   # R = int.from_bytes(os.urandom(8), byteorder="big")/((1 << 64) - 1)
   ## Increment counter for the bin
   j=0
   while j < B:  
      if (j*W<R and R<=(j+1)*W):
         A[j] = A[j] + 1
      j = j+1
   i = i+1

print (A)

### Calculate Chi-Squared statistic
# Chi-Squared statistic 
CHI = 0

# Expected value of all counters
EYi=N/B


j = 0
while j < B:
   CHI = CHI+ (A[j]-EYi) ** 2
   j = j+1

CHI = CHI/EYi

print (CHI)

print (1-chi2.cdf(CHI, B-1))


print(scipy.stats.chisquare(A, N/B, B-1))



