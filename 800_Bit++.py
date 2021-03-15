tc = int(input())
x = 0
for _ in range(tc):
    inp = input()
    if '+' in inp:
        x += 1
    else:
        x -= 1
print(x)


