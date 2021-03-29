for _ in range(int(input())):
    nums = list(map(int, input().split()))
    print("YES" if sum(nums)%9==0 and min(nums)>=sum(nums)//9 else "NO")