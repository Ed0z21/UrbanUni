
# Начальный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Простые числа
primes=[]
# Составные числа
not_primes=[]

for i in numbers:
    if i == 1:
        continue
    else:
        for j in primes:
            if i % j == 0:
                not_primes.append(i)
                break
        else:
            primes.append(i)
print(primes)
print(not_primes)