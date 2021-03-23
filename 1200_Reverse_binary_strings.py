import math

tc = int(input())
while tc:

    length = input()
    string = input()
    chars = [x for x in string]

    count = 0
    # count_max = 0
    for x in range(len(chars)-1):
        if chars[x] == chars[x+1]:
            count += 1

    print(math.ceil(count/2))

    tc-=1