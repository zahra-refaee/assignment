
n = int(input())
for i in range(2**n):
    l=[]
    for j in range(n):
        if i&2**j >0:
            l.append(j+1)
    print("{", end="")
    print(*l, sep =", ", end="} \n")