num = int(input())
hamburgers = list(map(int, input().split()))

high = -1
max_index = 0
for index in range(num):
    if hamburgers[index] > high:
        high = hamburgers[index]
        max_index = index + 1

hamburgers = sorted(hamburgers, reverse=True)
print(max_index, hamburgers[1])
