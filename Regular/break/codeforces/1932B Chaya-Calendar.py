for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))


    sign = a[0]

    for i in range(1,n):
        sign = ((sign // a[i]) + 1) * a[i]
        
    print(sign)