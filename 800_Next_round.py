n, k = map(int, input().split())
scores = list(map(int, input().split()))

count = 0
scores = sorted(scores)[::-1]
for score in scores:
    if 0 < score >= scores[k-1]:
        count += 1

print(count)