def primes(n):
    sieve=[1]*n
    sieve[0:2]=[0,0]
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n:i]=[0]*len(sieve[i*i:n:i])
    return [i for i,x in enumerate(sieve) if x]
print(primes(100))