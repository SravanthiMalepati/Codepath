import math 
def isPrime(n):
    if(n <= 1):
        return False
    if(n < 4):
        return True
    for i in range(2,int(math.sqrt(n) + 1)):
        if(n % i == 0):
            return False 
    return True
def nextprime(n):
    if n <= 1:
        return 2
    n += 1
    while(True):
        if(isPrime(n)):
            return n
        n += 1

print(nextprime(5))
print(nextprime(11))
print(nextprime(8))