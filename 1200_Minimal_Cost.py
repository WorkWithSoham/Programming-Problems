tc = int(input())
for _ in range(tc):
    n, v_cost, h_cost = map(int, input().split())
    ypoints = list(map(int, input().split()))
    cost = 0
    for y in range(0, len(ypoints)-1):
        if abs(ypoints[y+1] - ypoints[y]) >= 2:
            cost = 0
        if abs(ypoints[y+1] - ypoints[y]) == 1:
            cost = min(cost, min(v_cost, h_cost))
        if ypoints[y+1] == ypoints[y]:
            cost = min(cost, v_cost + min(h_cost, v_cost))
        print(cost)

