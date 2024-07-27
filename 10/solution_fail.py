primes = [3, 5, 7, 11, 13, 17, 19]

def gen_prime(primes):
    primes = primes.copy()
    for n in range(primes[-1]+2, primes[-1]**2, 2):
        if all(n % p for p in primes):
            yield n


primes.extend(gen_prime(primes))
primes.extend(gen_prime(primes))
for i in gen_prime(primes):
    if i >= 2000000:
        break
    primes.append(i)