def factorial(n):
    fact=1
    a=1
    for _ in range(n):
        yield fact
        a+=1
        fact*=a


for num in factorial(10):
    print(num,end=" ")
