for _ in range(int(input())):
    a,b = map(int,input().split())

    team = (a + b) // 4

    print(min(a,b) if min(a,b) < team else team)