lucky = []
for k in range(1, 10):
    for mask in range(2**k):
        a = ''
        for i in range(k):
            if (mask & (2**i)) != 0:
                a += '7'
            else:
                a += '4'

        lucky.append(int(a))

def solve():
    n = int(input())

    ans = 4
    for m in lucky:
        if m <= n:
            ans = max(ans, m)

    print(ans)

t = int(input())
for i in range(t):
    solve()