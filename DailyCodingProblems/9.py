'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def find_largest_sum(numbers: list) -> int:
    last, curr = 0, 0
    for num in numbers:
        last, curr = curr, max(curr, last+num)

    return curr

numbers = list(map(int, input().split()))
print(find_largest_sum(numbers))
