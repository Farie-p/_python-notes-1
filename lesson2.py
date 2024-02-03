# LESSON 2(TUPLES, FUNCTIONS,RETURN STATEMENT, IF STATEMENTS/ COMPARISONS
"""
A tuple is a type of data structure
similar to a list but has a few key differences from a list
it is unique
use ()parenthesis for a tuple
use []brackets for a list
it is immutable(can't change the values or modify it
can also create a list of tuples = [(4,7), (2,9), (3,1)]
it is easy to access the elements inside a tuple but can't be changed

####################### FUNCTIONS ##########################
 A function is basically a collection of code which performs a certain task.
 just call the function to perform the task
 use the key word def to define a function
 the code inside the function has to be called inorder to be executed
 --a parameter is a piece of information that is parsed in to a function (example) name,age
 -- say_Hi at the bottom is function calling
 -- can parse in as many parameters as needed.
 --
 ***def say_Hi(name, age):
    print('Hello ' + name)
***say_Hi('Mike')
################ RETURN STATEMENT #######################################
used to return the output from a function
no code is going to be executed after the return statement in a function
can be used to return any type of data structure

################# IF STATEMENTS ##################################
allow  programs to respond and do certain things.
are generally decisions taken throughout the day by humans
has conditions true or false, then make a decision

################# IF STATEMENTS AND COMPARISONS #########################
can compare all data types
either or -- logical or
both and -- logical and &&

##############DICTIONARIES #################################
 dictionaries  are a special structure which allows the user to store info in what is called key-value pairs
 example => word and meaning. in this case the word is the key and value
 whenever a dictionary is created in py {} curly brackets are used.
 keys are always unique
 the get f(x) can be used to specify a default value if the key is not found
 keys do not always have to be strings can put numbers as well

"""

coordinates = (3, 6)
print(coordinates[0])


# function
def say_Hi(name, age):
    print('Hello ' + name + ' you are ' + str(age))


say_Hi('Mike', 16)
say_Hi('Toby', 19)


def cube(num):
    return num * num * num


result = cube(4)
print(result)

is_female = False
is_short = False

if is_female and is_short:
    print('You are a female or short or both')
elif is_female and not is_short:
    print('You are a tall female')
elif not is_female and is_short:
    print('You are a short male')
else:
    print('You are neither a female nor short')


def max_num(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        return num_2
    else:
        return num_3


print(max_num(9, 6, 1))

print((6 + 9j).real)
print((6 + 9j).imag)
print(1.8e308)

########################### DICTIONARIES ##################################
monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}
print(monthConversions['Sep'])
print(monthConversions.get('Sep'))
print(monthConversions.get('Ot', 'Not a valid Key'))
