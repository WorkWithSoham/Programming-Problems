n, l = map(int, input().split())
lights = sorted(list(map(int, input().split())), reverse=True)

max_dif = 0

for i in range(len(lights)-1):
    max_dif = max(max_dif, lights[i]-lights[i+1])

print(format(max(max_dif/2, lights[-1], l-lights[0]), '.10f'))