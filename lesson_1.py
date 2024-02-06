"""
1ST LESSON IN PYTHON
VARIABLES, DATA TYPES, lists, list functions

- numbers, string, boolean (3 basic data types)
- the user can create variable containers.
- can convert a number into a string
- can perform arithmetic operations ( use the % to get the remainder)
- there are 3 types of number data types(int, float, )
- Python is a case-sensitive language
- other math operations include finding the( maximum, minimum, absolute, power, rounding off, floor, ceiling and square root) as shown below
- 
"""

############    VARIABLES  ##########################
#STRING, NUMBERS (all different types of numbers), BOOLEAN

# declaring variables

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
print(a + b)
print(b - a)
print(a - b)
print(a * b)
########## INPUT FROM THE USER############################

name = input("Enter your name: ")
age = input('Enter your age: ')
print('Hello, my name is ' + name + ' and I am ' + age + '.')
print(f'Hello, my name is {name} and I am {age}.')
#############   STRING FUNCTIONS ###########################################
"""
- string functions include (uppercase, lowercase, replace
- the user can use the curly braces to print out the input, 
   but they should also include the f function for the output to come out as expected without an error
- the user can 
            .. find the index of a letter in a string
            .. output a specific part of the string by using index values
            .. output specific letters in a string
            .. find the length of the string
            .. replace letters or words in a string
"""
print(c.upper())
print(c.upper().islower())
print(c[1:12])
print(len(c))
print(c.index("s"))
print(c.replace("string", "sentence"))

######################### IF ELSE STATEMENTS ################################################
if a * b == b * a:
    print('the output is the same on both sides of the equal sign')
else:
    print('gives an answer with different values on both sides of the equal sign')
if a - b == b - a:
    print('a minus b gives the same answer as b minus a on both sides of the equal sign')
else:
    print('it gives a dif answer on both sides of the equal sign')

num1 = input('enter a number:')
num2 = input('enter another number:')
result = int(num1) + float(num2)

print(result)

##################### lists basics ##########################################

"""
- lists use square brackets[]
- lists for multiple values inside an object
- the user can store any piece of data, numbers, strings, boolean, etc.
- use an index to access data in the list
- use a negative index  of 1 [-1] to access data at the end of the list 
- use an index and a colon: to access info from the index to the end of the list [3:]
- use a negative index and a colon [-3:]to access data from the end of the list but the output comes in the same order as the positive input
- use the index with a starting point and a finishing [1:n] point, gives an output from the starting index up to the index before the finishing index (n-1) {range}
- can modify the list by accessing the index and changing the value of that index
 ################# list functions ################
 1. extend function😂
     - allows the user to add more values to the list, and may also concatenate 2 lists together
 2. append function😂
     - allows the user to append individual items to the end of the list
 3. insert function😂
     - allows the user to insert an item anywhere inside the list and all the other elements are pushed to the right
 4. remove function😂
     - allows the user to remove element/s from the list, just remove the element with its name and not the index
 5. clear function 😂
     - it clears all the elements from the list, returns an empty list
 6. pop function😂
     - removes the last element in the list
 7. reverse function😂
     - reverses the order of the elements in the list
 8. copy function😂
     - allows the user to copy a list forming another list
 """

dogs = ['Tiger', 'Bruce', 'Sophie', 'Whiskey']
lottery_numbers = [3, 5, 7, 9, 11]
dogs[1] = 'Mimi'
print(dogs)
print(dogs[2])
print(dogs[-1])
print(dogs[1:])
print(dogs[-2:])
print(dogs[1:3])
dogs.extend(lottery_numbers)
print(dogs)
dogs.append('Mimi')
print(dogs)
dogs.insert(2, 'Pippy')
print(dogs)
dogs.remove('Mimi')
print(dogs)
dogs.remove(7)
print(dogs)
dogs.pop()
print(dogs)
print(dogs.index(9))
print(dogs.index('mike'))
#dogs.clear() remove all the elements in dogs.
print(dogs)
print(lottery_numbers)
lottery_numbers.reverse()
print(lottery_numbers)
lottery_numbers_2 = lottery_numbers.copy()
print(lottery_numbers_2)
lottery_numbers.extend(lottery_numbers_2)
print(lottery_numbers)
