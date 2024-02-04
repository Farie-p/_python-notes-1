# LESSON 2(TUPLES, FUNCTIONS,RETURN STATEMENT, IF STATEMENTS/ COMPARISONS
"""
 - A tuple is a type of data structure similar to a list but has a few key differences from a list
 - it is unique and uses ()parenthesis
 - it is immutable(can't change the values or modify once they are declared.
 - it is possible to create a list of tuples => [(4,7), (2,9), (3,1)]
 -  the elements are easily accessible in a tuple but can't be changed

####################### FUNCTIONS ##########################
  - A function is a collection of code that performs a certain task.
  - It has to be called in order to perform a task/executed
  - use the keyword def to define a function
  - a parameter is a piece of information that is parsed into a function (example) name and age below
  - say_Hi  is a function calling. see the code below
  - can parse in as many parameters as needed.
  - the str in the function below, changes the data type from string to output a number
  
  """
 
  def say_Hi(name, age):
     print('Hello ' + name + 'you are ' + str(age))
  say_Hi('Martha', 25)
 
################ RETURN STATEMENT #######################################
 """
  - the return statement is used to return the output from a function
  - no code is going to be executed after the return statement in a function
  - can be used to return any type of data structure

################# IF STATEMENTS ##################################
 - allow  programs to respond and do certain things.
 - they are generally decisions taken throughout the day by humans
 - has conditions true or false, then make a decision

################# IF STATEMENTS AND COMPARISONS #########################
 - can compare all data types
 - either or -- logical or
 - both and -- logical and &&

############## DICTIONARIES #################################
 - dictionaries  are a special structure that allows the user to store info in what is called key-value pair/s
 - example => a word and a meaning. in this case, the word is the key and the meaning is the value
 - whenever a dictionary is created in Python { } curly brackets are used.
 - the keys are always unique
 - the get function can be used to specify a default value if the key is not found
 - keys do not always have to be strings, numbers can be used as well

"""
################## tuple #################################
coordinates = (x, y)
print(coordinates[0])


##################### function ############################
def say_Hi(name, age):
    print('Hello ' + name + ' you are ' + str(age))


say_Hi('Mike', 16)
say_Hi('Toby', 19)

##################### return statement #########################
def cube(num):
    return num * num * num

result = cube(4)
print(result)

############# if else comparisons ####################################

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
weekConversions = {
    'Mon': 'Monday',
    'Tue': 'Tuesday',
    'Wed': 'Wednesday',
    'Thur': 'Thursday',
    'Fri': 'Friday',
    'Sat': 'Saturday',
    'Sun': 'Sunday'
    
}
print(weekConversions['Sun'])
print(weekConversions.get('Wed'))
print(weekConversions.get('Frid', 'Not a valid Key'))
