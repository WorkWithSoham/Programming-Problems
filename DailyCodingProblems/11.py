'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

words = [x for x in input().split()]

while True:
    string = input()
    suggestions = []
    for word in words:
        if string == word[:len(string)]:
            suggestions.append(word)

    print(suggestions)

