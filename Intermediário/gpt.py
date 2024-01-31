'''
- Write a program that prompts the user to enter three numbers, and then sorts them in ascending order.
'''

#def numbers(number):
#    three_numbers = []

#    for i in range(number):
        
#        while True:
#            user_input = input(f'digite o {i+1}º numero: ')
#            try:
#                three_numbers.append(float(user_input.replace(',', '.')))
#                break
#            except ValueError:
#                print('digite apenas numeros validos')
#    return sorted(three_numbers)
    


#print('digite 3 numeros 1 de cada vez')
#print('numeros ordenados', numbers(3))

'''
- Given a list of integers, sort it in descending order.
'''

#integers = [86, 236, 12]

#integers.sort(reverse = True)
#print(integers)

'''
- Write a program that sorts a string in alphabetical order.
'''

#def alphabetical():
#    word = input('digite uma palavra: ')
#    return sorted(word)

#print(alphabetical())


'''
- Given a list of strings, sort it in reverse alphabetical order.
'''

#def alphabetical(*args):
#    alphabetical_list = []
#    for word in args:
#        alphabetical_list.append(sorted(word, reverse = True))
#    return alphabetical_list

#print(alphabetical('marrom', 'mozuda', 'julian', 'julia'))

'''
Intermediate exercises:
- Write a program that reads a file containing a list of words and prints them in alphabetical order. Use the sort() method to sort the list.

- Given a list of dictionaries representing people with their age and height, sort the list by age and then by height.
'''
by_age = ''
by_height = ''

person = [
    {
        'nome': 'Marrom',
        'idade': 5,
        'altura': 0.5
    },
    {
        'nome': 'Julian',
        'idade': 0.4,
        'altura': 0.1
    },
        {
        'nome': 'Julia',
        'idade': 0.3,
        'altura': 0.15
    },
        {
        'nome': 'Mozuda',
        'idade': 150,
        'altura': 1.6
    },
        {
        'nome': 'theo',
        'idade': 0.3,
        'altura': 0.1
    },
]

def age_height(person):
    for item in person:
        print(item)
    print()

by_age = sorted(person, key = lambda item: item['idade'])

by_height = sorted(person, key = lambda item: item['altura'])

by_age_height = sorted(person, key = lambda item: (item['idade'], item['altura']))

by_height_age = sorted(person, key = lambda item: (item['altura'], item['idade']))

age_height(by_age)
age_height(by_height)
age_height(by_age_height)
age_height(by_height_age)


'''
- Write a program that reads a CSV file containing information about people (name, age, and occupation), sorts the information by age in ascending order, and then writes it to a new CSV file.

- Write a program that reads a file containing a list of numbers, sorts them in ascending order, and writes the sorted numbers to a new file.
'''