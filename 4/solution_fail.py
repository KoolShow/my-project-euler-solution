primes = []
for i in range(3, 999, 2):
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
            n /= p

def solve(factors):
    m = factors.pop()
    mult_max = 999//m
    mult_max = [1,2,3,3,5,5,7,7,7][mult_max-1]

    n = 1
    left = []

    for i in factors:
        if i > mult_max:
            n*=i
        else:
            left.append(i)
    if n > 999:
        return False
    if n < 100:
        if not left:
            return False
    n_mult_max = 999//n
    n_mult_max = [1,2,3,3,5,5,7,7,7][mult_max-1]
    for i in left:
        if i > n_mult_max and i > mult_max:
            return False
    print(f"unsolved: {n=}, {m=}, {left=}")




for i in range(997, 100, -1):
    n = int(str(i) + str(i)[::-1])
    factors = list(factor(n))
    if len(factors) == 1:
        continue
    if any(i>999 for i in factors):
        continue
    if len(factors) == 2:
        a, b = factors
        if a<100: continue
        break
    if (res := solve(factors)):
        a, b = res
        break

print(f"{a = }")
print(f"{b = }")
print(f"Ans = {a * b = }")
