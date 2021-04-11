n, m = map(int, input().split())
name_num = list(map(int, input().split()))

count = []
total_num = 0
page_num = 0
for num in name_num:
    total_num += num
    count.append(total_num//m - page_num)
    page_num = total_num//m

print(' '.join(map(str, count))) 