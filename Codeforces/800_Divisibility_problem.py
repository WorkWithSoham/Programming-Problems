tc = int(input())
for _ in range(tc):
    a, b = map(int, input().split())
    if a%b==0:
        print(0)
    else:
        print((((a//b)+1)*b) - a)

