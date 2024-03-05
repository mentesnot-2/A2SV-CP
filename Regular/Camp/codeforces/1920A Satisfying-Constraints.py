for _ in range(int(input())):
    n = int(input())
    instruction = []
    one = float("-inf")
    two = float("inf")
    three = set()
    for i in range(n):
        a,b = map(int,input().split())
        if a == 1:
            one = max(one,b)
        elif a == 2:
            two = min(two,b)
        else:
            three.add(b)
    
    if two < one:
        print(0)
        continue
    total = two - one + 1
    for i in three:
        if one <= i <= two:
            total-=1

    print(total)

