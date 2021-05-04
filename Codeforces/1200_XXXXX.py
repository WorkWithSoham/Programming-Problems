def checkSum(l):
    return sum(l)%x != 0

tc = int(input())
while(tc):

    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    max_len = -1
    for i in range(n):
        s += arr[i]
        if s % x != 0:
            max_len = max(max_len, max(len(arr)-i-1, i+1))
    
    print(max_len)
    tc -= 1
