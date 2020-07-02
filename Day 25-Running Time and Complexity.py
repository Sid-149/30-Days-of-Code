# Enter your code here. Read input from STDIN. Print output to STDOUT
'''def isprime(n):
    if n > 1:
        for j in range(2, n):
            if n % j == 0:
                return 'Not Prime'
                break
        else : return 'Prime'
    else: return 'Not Prime'
    
T = int(input())
for i in range(T):
    n = int(input())
    print(isprime(n))
'''
from math import sqrt
def isprime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i is 0:
            return False
    return True

T = int(input())
for i in range(T):
    n = int(input())
    if n >= 2 and isprime(n):
        print('Prime')
    else: print('Not prime')
