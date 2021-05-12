'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''
def check_value(n):
    return 1 if 0 < int(n) < 27 else 0

def decode_count(num):
    if len(num) == 1:
        return 1
    elif len(num) == 2:
        return 1 + check_value(num)
    else:
        if not check_value(num[:2]):
            return 1
        else:
            return 1 + decode_count(num[1:])

number = input()
ans = decode_count(number)

print(ans)