user = int(input("Enter an integer: "))
prime_numbers = []

for i in range(2, user):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)

print(sum(prime_numbers))
