from random import randint, getrandbits
from generateRandomPrimeInteger import generateRandomPrime
from math import gcd

def generate(p,q,N):
  x=0
  while(not gcd(N,x)==1):
    x=randint(0,N)
  return pow(x,2)%N

def generateBits(list, amount):
  generatedValues = []

  p = list[0]
  q=list[1]
  N = p*q

  bitsArray = []
  # amount += 1

  for i in range(amount):
    generatedValue=generate(p,q,N)
    generatedValues.append(generatedValue)

    if(generatedValue%2 == 0):
      bitsArray.append(0)
    else:
      bitsArray.append(1)
  
  return bitsArray