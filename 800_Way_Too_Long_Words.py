tc = int(input())
for _ in range(tc):
    string = input()
    if len(string) > 10:
        print(string[0] + str(len(string[1:-1])) + string[-1])
    else:
        print(string)