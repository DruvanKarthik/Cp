def prime(n):
    if n==0 or n==1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n+1/2)):
        if n%i==0:
            return False
    return True
count_prime=0
for i in range(1000):
    if prime(i):
        count_prime+=1
    else:
        continue
print(count_prime)