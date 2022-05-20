# Largest prime factor
i = 2
result = []

while i <= 36 / 2:
    if i % 1 == 0:
        result.append(i)
    i += 1
print(result)
