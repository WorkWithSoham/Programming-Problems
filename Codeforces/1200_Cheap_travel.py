n, m, a, b = map(int, input().split())

min1 = (n//m)*b + (n%m)*a
min2 = n//a

ans = min(min1, min2)
print(ans)
