def find_depth(numbers, depth):
    if len(numbers) == 0:
        return []
    max_n_index = 0
    for index in range(len(numbers)):
        if numbers[index] == max(numbers):
            max_n_index = index
            break
    numbers[max_n_index] = depth
    depth += 1
    return find_depth(numbers[:max_n_index], depth) + [numbers[max_n_index]] + find_depth(numbers[max_n_index+1:], depth)

tc = int(input())
while tc:
    
    n = int(input())
    numbers = list(map(int, input().split()))
    print(*find_depth(numbers, 0))

    tc -= 1

