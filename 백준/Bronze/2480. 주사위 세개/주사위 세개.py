import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))

if lst[0] == lst[1] == lst[2]:
    print(10000 + lst[0] * 1000)
elif lst[0] == lst[1] != lst[2]:
    print(1000 + lst[0] * 100)
elif lst[0] == lst[2] != lst[1]:
    print(1000 + lst[0] * 100)
elif lst[1] == lst[2] != lst[0]:
    print(1000 + lst[1] * 100)
elif lst[0] != lst[1] != lst[2]:
    print(max(lst) * 100)