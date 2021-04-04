tc = int(input())
while tc:
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers_copy = numbers.copy()

    for index in range(len(numbers)-1):
        if numbers[index] == numbers[index + 1]:
            numbers_copy.remove(numbers[index])

    min_count = 20000000
    numbers_copy_set = list(set(numbers))

    for index in range(len(numbers_copy_set)):
        min_count_index = numbers_copy.count(numbers_copy_set[index]) + 1
        if numbers_copy_set[index] == numbers_copy[0]:
            min_count_index -= 1
        if numbers_copy_set[index] == numbers_copy[-1]:
            min_count_index -= 1

        min_count = min(min_count, min_count_index)
    print(min_count)
    tc -= 1