def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def findPrime(beginning, finish):
    for j in range(beginning, finish):
        if isPrime(j):
            return j

def encrypt ():
    print("Provide two integers")
    x = int(input())
    y = int(input())
    prime1 = findPrime(x, y)
    print("Provide two integers")
    x = int(input())
    y = int(input())
    prime2 = findPrime(x, y)
    return prime1*prime2

print(encrypt(), encrypt())


#x = 32
#y = 35

#print(f"The prime between {x} and {y} is {findPrime(x,y)}")



#print("What is the number?")
#x = int(input())
#if isPrime(x):
#    print(f"The number {x} is prime!")
#else:
#    print("The number was not prime!")
