def big_swap(num: list):
    return num[len(num)//2:] + num[:len(num)//2]

def alt_swap(num: list):
    alt_num = num.copy()
    for i in range(0, len(alt_num)-1, 2):
        alt_num[i], alt_num[i+1] = alt_num[i+1], alt_num[i]
    return alt_num

# def sort_check(num: list):
#     return num == sorted(num) or num == ref_nums

n = int(input())
nums = list(map(int, input().split()))
count_a = 0
count_b = 0
copy_nums = nums.copy()
ref_nums = nums.copy()

while copy_nums != sorted(copy_nums):
    if copy_nums == sorted(ref_nums):
        break
    copy_nums = big_swap(copy_nums)
    count_b += 1 
    if copy_nums == sorted(copy_nums):
        break
    if copy_nums == ref_nums:
        count_b = -1
        break
    copy_nums = alt_swap(copy_nums)
    count_b += 1 
    if copy_nums == sorted(copy_nums):
        break
    if copy_nums == ref_nums:
        count_b = -1
        break

while nums != sorted(nums):
    if nums == sorted(ref_nums):
        break
    nums = alt_swap(nums)
    count_a += 1
    if nums == sorted(nums):
        break
    if nums == ref_nums:
        count_b = -1
        break
    nums = big_swap(nums)
    count_a += 1  
    if nums == sorted(nums):
        break
    if nums == ref_nums:
        count_b = -1
        break

print(min(count_a, count_b))

