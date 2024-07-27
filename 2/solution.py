even_fib = [1, 2]

while even_fib[-1] < 4000000:
    even_fib.append(even_fib[-1] + even_fib[-2])

even_fib.pop()

Ans = sum(filter(lambda x: x % 2 == 0, even_fib))

print(f"{Ans = }")