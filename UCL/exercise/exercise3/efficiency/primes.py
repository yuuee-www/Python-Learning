primes = []
for test in range(2,100000):
    is_prime = True

    for p in primes:
        if test % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(test)
print("Found ", len(primes), "primes")
