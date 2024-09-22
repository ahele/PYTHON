def find_divisors(n):
    divisors = []
    x =(i for i in range(1,n+1) if n % i == 0) 
    divisors.append(x)
    print(divisors)

find_divisors(6)