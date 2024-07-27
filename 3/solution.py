N = 600851475143

primes = []
for i in range(3, int(N**0.5)+1, 2):
    is_prime = True
    for prime in primes:
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
primes = [2] + primes

Ans = 1

factors = []

for p in primes[::-1]:
    if N % p == 0:
        Ans = p
        break

print(f"{Ans = }") # Ans = 6857