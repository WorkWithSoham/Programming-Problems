for _ in range(int(input())):
    n=int(input())
    a=-1
    x=0
    while x<=n:
        a+=1
        k=2**(a+1)-1
        x+=k*(k+1)//2
    print(a)