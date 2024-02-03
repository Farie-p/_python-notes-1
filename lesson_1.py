"""1ST LESSON IN PYTHON
VARIABLES, DATA TYPES, lists, list functions
numbers, string, boolean (3 basic data types)
u can create variable containers.
can convert a number into a string
"""

############    VARIABLES  ##########################
#STRING, NUMBERS (all dif types of number), BOOLEAN

a = 10
b = 9.8
d = -7
c = "just a string"
is_number = True
is_string = False
#############  NUMBERS  ##############################################
print(-a * a / b)
print(a % 4)
print(str(a) + " is my fav num")
print(abs(d))
print(pow(d, 2))
print(max(d, 9))
print(min(a, 6))
print(round(3.51036))
print(floor(3.51036))
print(ceil(3.507389))
print(sqrt(11000))
print(a+b)
print(b-a)
print(a-b)
print(a*b)
########## INPUT FROM THE USER############################

name = input("Enter your name: ")
age = input('Enter your age: ')
print('Hello ' + name + ' you are ' + age + '.')

#############   STRING FUNCTIONS ###########################################
print(c.upper())
print(c.upper().islower())
print(c[1:12])
print(len(c))
print(c.index("s"))
print(c.replace("string", "sentence"))

#########################################################################
if a*b == b*a:
    print('the answer is the same')
else:
    print('the answer is different')
if a-b == b-a:
    print('a minus b gives the same answer as b minus a')
else:
    print('it gives a dif ans')

num1 = input('enter a number:')
num2 = input('enter another number:')
result = int(num1) + float(num2)

print(result)

##################### lists basics ##########################################

lists use square brackets
lists for multiple values inside an object
can store any piece of info, numbers, strings, boolean etc.
use index to access info in the list
use negative index to access info in the list from the far right of the list
use an index and a colon : to access info from the index to the end of the list
use a negative index and a colon : to access from the back of the list but the
 output comes in the same order as the positive input
use the index with a starting point and a finishing [1:n] point,
 but it only outputs from the starting index up to the index which is 
 before the finishing index (n-1) {range}
can modify the list by accessing the index and can change the value of that index
 ################# list functions ################
 1. extend f(x)
 allows the user to add more values to the list , may also concatenate 2 lists together
 2. append f(x)
 allows the user to append individual items to the end of the list
 3. insert f(x)
 allows the user to insert an item anywhere inside the list and all the other
  elements are pushed to the right
 4. remove f(x)
 allows the user to remove element/s from the list, just remove the element with its name
 and not the index
 5. clear f(x)
 it clears all the elements from the list, returns an empty list
 6. pop f(x)
 removes the last element in the list
 7. reverse f(x)
 reverses the order of the elements in the list
 8. copy f(x)
 allows the user to copy a list forming another list

dogs = ['tiger', 'bruce', 'sophie', 'whiskey']
lottery_numbers = [3, 5, 7, 9, 11]
dogs[1] = 'mimi'
print(dogs)
print(dogs[2])
print(dogs[-1])
print(dogs[1:])
print(dogs[-2:])
print(dogs[1:3])
dogs.extend(lottery_numbers)
print(dogs)
dogs.append('mimi')
print(dogs)
dogs.insert(2, 'black')
print(dogs)
dogs.remove('mimi')
print(dogs)
dogs.remove(7)
print(dogs)
dogs.pop()
print(dogs)
print(dogs.index(9))
print(dogs.index('mike'))
#dogs.clear()
print(dogs)
print(lottery_numbers)
lottery_numbers.reverse()
print(lottery_numbers)
lottery_numbers_2 = lottery_numbers.copy()
print(lottery_numbers_2)
lottery_numbers.extend(lottery_numbers_2)
print(lottery_numbers)"""
