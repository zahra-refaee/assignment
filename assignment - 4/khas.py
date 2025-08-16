def sum_digits(n):
    res=0
    while n>0:
        res+= n%10
        n//=10
    return res

def special(n):
     return sum_digits(n)%7 == 0
   

n = int(input())
n = n+1
while not special(n):
    n=n+1
print(n)
    