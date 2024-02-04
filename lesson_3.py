############## LOOPS ##########################
# WHILE LOOP

"""
############### WHILE LOOP####################
A while loop is a structure which allows the user to loop through and execute a
block of code multiple times until a certain condition is met

############ FOR LOOP #################################
provide a specific purpose

"""
############# WHILE LOOP################################
i = 1
while i <= 10:
    print(i)
    i += 1

print('Done looping')

############## FOR LOOP ################################
for letter in 'Handidzokeri Shure':
    print(letter)

shamwari = ['Tindo', 'Memo', 'Tawanda','Pamela']
len(shamwari)
for shamwari in shamwari:
    print(shamwari)

for index in range(5, 10):
    print(index)
############## EXPONENT FUNCTION #######################
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2,5))

################### 2D LISTS AND NESTED LOOPS########################
number_grid =[
    [2, 3, 4],
    [1, 5, 7],
    [6, 8, 9],
    [0]
]
print(number_grid[0][0])
for row in number_grid:
    for col in row:
        print(col)
############ translate function


def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in 'aeiou':
            if letter.isupper():
                translation = translation + 'M'
            else:
                translation = translation + 'm'
        else:
            translation = translation + letter
    return translation


print(translate(input('Enter a phrase')))
