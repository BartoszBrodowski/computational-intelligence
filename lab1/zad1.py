import math

def prime(n):
    if n <= 0:
        return False
    sqrt =  math.sqrt(n)
    for number in range(2, math.ceil(sqrt) + 1):
        if n % number == 0:
            return False
        else:
            continue
    return True

def select_primes(x):
    return list(filter(prime, x))


print(select_primes([1,2,4,13,7,8]))

