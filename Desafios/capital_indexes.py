#Capital indexes
#Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

#For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

indexes = []

def capital_indexes(string):
    indexes.clear()
    for index, letter in enumerate(string):
        if letter.isupper():
            indexes.append(index)
    return indexes

print(capital_indexes('HeLlO'))
print(capital_indexes('WorLd'))

# or

from string import ascii_uppercase

def capital_indexes(string):
    indexes.clear()
    return [i for i in range(len(string)) if string[i] in ascii_uppercase]

print(capital_indexes('HeLlO'))
print(capital_indexes('WorLd'))