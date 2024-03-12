import math
tc = int(input())

for _ in range(tc):
    n,P,l,t = map(int,input().split())

    start = 0
    end = n
    weeks = (n + 6) // 7
    def calc(k) :
        return k * l + min(weeks,2*k) * t

    while end - start > 1:
        mid = (start +  end)//2

        if calc(mid) >= P:
            end = mid
        else:
            start = mid

     
    
    print(n - start - 1)


    