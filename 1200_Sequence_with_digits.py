for _ in range(int(input())):
    num, k = map(int, input().split())
    for _ in range(k-1):
        digits = [int(x) for x in str(num)]
        num = num + min(digits) * max(digits)
    print(num)
