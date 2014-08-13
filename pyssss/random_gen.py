from prime import MillerRabinTest
import os

def GenerateRandomNumber(_min,_max):
    x = 0
    b_len = 8192
    while(1):
        a = os.urandom(b_len)
        a = int(a.encode('hex'),16)
        b = os.urandom(b_len)
        b = int(b.encode('hex'),16)
        x = (((a^b)%(_max+_min)) + _min)
        if min(a,b) < _min:
            b_len = b_len * 2
            print "** random module warning ** Increasing pool size to", b_len,"bytes..."
        else:
            return x
def GenerateRandomPrimeNumber(_min,_max):
    while(1):
        x = GenerateRandomNumber(_min,_max)
        if MillerRabinTest(x):
            if (x >= _min) and (x < _max):
                return x
            else:
                x = GenerateRandomNumber(_min,_max)
        else:
            x += 1
