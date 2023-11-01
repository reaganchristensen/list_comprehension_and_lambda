''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evennumbers = list(filter(lambda num: num % 2 == 0, numbers))
print(evennumbers)

oddnumbers = list(filter(lambda num: num % 2, numbers))
print(oddnumbers)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = list(filter(lambda num: len(num) == 6, weekdays))
print(days)

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
original = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove = ['orange', 'black']

removedlist = list(filter(lambda num: num not in remove, original))
print(removedlist)

''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

newlist = list(filter(lambda num: num not in list2, list1))
print(newlist)

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

original = ['red', 'black', 'white', 'green', 'orange']
ack = list(filter(lambda num: 'ack' in num, original))
abc = list(filter(lambda num: 'abc' in num, original))
print(ack)
print(abc)

''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
verify = lambda s: all((
len(s) >= 8,
any(c.isupper() for c in s),
any(c.islower() for c in s),
any(c.isdigit() for c in s)))

str1 = "Hello8world"
print(verify(str1))
str1 = "HELLO"
print(verify(str1))
str1 = "hello"
print(verify(str1))

''' 7)
Write a Python program to sort a list of tuples using Lambda.

#Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_scores.sort(reverse = False, key = lambda num: num[1])
print(original_scores)