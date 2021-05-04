'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

k = int(input())
L = [int(x) for x in input().split()]
ans: bool = False
for element in L:
    if (k - element) in L:
        ans = True
        break

print(ans)
