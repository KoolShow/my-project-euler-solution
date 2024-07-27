primes = []
for i in range(3, 104744 , 2):
    is_prime = True
    for prime in primes:
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

primes = [2] + primes
print(f"Ans = {primes[10001-1]}") # Ans = 104743