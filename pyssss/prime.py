import random 

def mod_exp(a,e,m):
  return pow(a,e,m)

def _decompose_mr(n):
  '''private routine for MillerRabinTest
     decompose n as ((2**s)*t). Returns s and t'''
  s=0
  t=0
  while((t%2)==0):
    s+=1
    t=(n-1)/(2**s)
  return s,t

def _test_mr(n,s,t):
  '''private routine for MillerRabinTest
     single test'''
  a = random.randint(1,n-1)
  redux = mod_exp(a,t,n)
  if (redux == 1) or (redux == (n-1)):
    return True
  for i in xrange(1,s):
    if ((mod_exp(a,((2**i)*t),n)) == (n-1)):
      return True
  return False

def MillerRabinTest(n,k=100):
  '''Miller-Rabin Primality Test.
     Returns False if n is composite, True if n is probably prime (with prob <= 1/(4^k))'''
  if n == 1:
    return False
  if n == 2:
    return True
  if (n%2) == 0:
    return False
  s,t=_decompose_mr(n)
  res=True
  while(k>0):
    if res == False:
      break
    res=_test_mr(n,s,t)
    k-=1
  return res
