
import random
import math

###function to check prime or not
def is_prime(n):
    if(n > 1):
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                return False
        return True
    else:
        return False

###random cnt number of primes
def  generate_random_number(cnt,n1, n2,):
    primes=[]
    for i in range(n1,n2):
        if(is_prime(i)):
            primes.append(i)
    random_items=random.sample(primes,k=cnt)
    return random_items

###to get number of primes in the n1 and n2
def number_of_prime_int_the_range(n1,n2):
    primes=[]
    for i in range(n1,n2):
        if(is_prime(i)):
            primes.append(i)
    return len(primes)

###while loop till corrent inputs entered
while True:
    print("Provide inputs of 3 integers from the keyboard:")
    print("The 1st is the number of unique prime numbers to be created;")
    print("The 2nd and 3rd definr the range of those prime numbers")
    x=input("enter those 3 integers separated by space ")
    out=list(map(int,x.split(" ")))
    num1=out[0]
    num2=out[1]
    num3=out[2]

    if(num2>num3 or number_of_prime_int_the_range(num2,num3)<num1):
        print("****improper input was provided; try again")
        print()
    else:
        print("The generated random number list:")
        arr=generate_random_number(num1,num2,num3)
        print(arr)
        print("The reversed order:")
        arr.reverse()
        print(arr)
        print("The sorted order:")
        arr.sort()
        print(arr)
        mini=min(arr)
        maxi=max(arr)
        print("The minimum and maximum prime numbers are : ",mini,"and ",maxi)
        break
        
        
          
