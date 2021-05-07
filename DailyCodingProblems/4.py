'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

numbers = [int(x) for x in input().split() if int(x) > 0] + [0] # get 1 as output if all are negative

for i in range(1, max(numbers)+2): # max(numbers) + 2 => we want to get the next number in case all the earlier are present
    if i not in numbers:
        print(i)
        break
