for _ in range(int(input())):
    n, m = map(int, input().split())
    numbers = sorted([x%m for x in list(map(int, input().split()))]) 
    count = 0
    for i in range(m):
        if numbers.count(i) - numbers.count(m-i):
            count += 1
            # print(count)
        else:
            count += abs(numbers.count(i) - numbers.count(m-i)))
            # print(count)
        if numbers.count(m-i):
            numbers.remove(m-i)
    print(count)

