# Multiples of 3 or 5 
x = sum(i for i in range(10) if i % 3 == 0 or i % 5 == 0)
print(x)