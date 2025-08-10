import math

n = int(input())

if n < 2:
    print('NO')
    exit(0)

for i in range(2, int(math.sqrt(n) + 1.1)):
    if n % i == 0:
        print('NO')
        exit()

print('YES')