import math
# Sieve of Sundaram
def SoS(n):
    k=(n-2)//2
    integers_list=[True]*(k+1)
    for i in range(1,math.floor(k**(1/2))):
        j=i
        while i+j+2*i*j<=k:
            integers_list[i+j+2*i*j]=False
            j+=1
    # Print primes
    if n>2:
        print(2)
    for i in range(1,k+1):
        if integers_list[i]==True:
            print(2*i+1)

n=1000
SoS(n)
