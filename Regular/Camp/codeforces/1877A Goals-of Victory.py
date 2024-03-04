for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    neg_sum = sum([i for i in a if i < 0])
    pos_sum = sum([i for i in a if i > 0])
    neg_sum = (-1) * neg_sum
    print((neg_sum - pos_sum))