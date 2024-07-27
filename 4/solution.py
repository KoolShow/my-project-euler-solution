palindrome = {int(str(i) + str(i)[::-1]) for i in range(997, 100, -1)}
product = {i*j for i in range(997, 100, -1) for j in range(997, i-1, -1)}

print("Ans =", max(palindrome & product)) # Ans = 993 * 913 = 906609