from math import ceil, sqrt

primes = []
for i in range(3, ceil(sqrt(20))+1 , 2):
    is_prime = True
    for prime in primes:
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

primes = [2] + primes

def factor(n):
    for p in primes:
        while n % p == 0:
            yield p
            n //= p
    if n != 1:
        yield int(n)

def count(n):
    factors = {}
    for f in factor(n):
        if f in factors:
            factors[f] += 1
        else :
            factors[f] = 1
    return factors

factors = {}

for i in range(1, 21):
    for k,v in count(i).items():
        if k in factors:
            factors[k] = max(factors[k], v)
        else:
            factors[k] = v

N = 1
for k,v in factors.items():
    N *= k**v

print(f"Ans = {N}") # Ans = 232792560