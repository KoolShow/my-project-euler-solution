for a in range(1, 334):
    for b in range(a, 665):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("Ans =", a*b*c) # Ans = 31875000
            break
