sup = 1000 - 1

sup_5x = sup//5
sup_3x = sup//3
sup_15x = sup//15

sum_of_5x = 5*sup_5x*(sup_5x+1)//2
sum_of_3x = 3*sup_3x*(sup_3x+1)//2
sum_of_15x = 15*sup_15x*(sup_15x+1)//2

Ans = sum_of_5x + sum_of_3x - sum_of_15x

print(f"{Ans = }") # Ans = 233168