numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] > 1:
        if (numbers[i] % 2 != 0 or numbers[i] == 2) and (numbers[i] % 3 != 0 or numbers[i] == 3):
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print('Primes:', primes)
print('Not Primes:', not_primes)
