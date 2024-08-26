n = int(input("Enter the number"))
f=1
i=1

while 0<i<=n:
    f=(f*n*(n-1))
    i=i+1
    n=n-2

    print(f)
