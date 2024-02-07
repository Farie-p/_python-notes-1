# Catching errors TRY/EXCEPT
"""
#########################    TRY EXCEPT   #####################
Error handling function where the user tries running the code and if it does not
execute, it gives an option to handle the error
This is basically to try and protect the program
the 'except' catches any error
the 'except' can also catch a specific type of error e.g division by zero
or invalid input
the user can also print out the error by its name SEE err.
the user should catch specific errors and not everything

#########################    READING FILES   #####################
allows the user to read info from files outside the python file e.g html, txt or CSV
the user can use the 'r' mode which is only for reading
the user can use the 'w' mode wc is only for writing
the user can use the 'a' mode wc is only for appending i.e adding info to the end of the file
the user can use the 'r+' mode wc is for reading and writing

the .readable function is to see whether the file is readable
the .read function is to print out all the contents of the file
the .readline function is to read the first line in the file, if this is printed out
 twice it reads from the first 2 lines of the file
the .readlines function is to read multiple lines in the file
if the user wants to read a specific line in the file, they have to include the
 index value of that line[]
can also use loops to parse through the file
#################### WRITING TO FILES#####################################
WRITING AND APPENDING TO FILES {AAA}
-if the user add some data to the file by appending, it is saved to the file,
 and if you run the code again the same data that has been added will be added again(repetition )
 and potentially causing errors. One should be careful when appending to files.
to append some more information, the user should use the '\n' function inorder to add a new line
in addition to appending, the user can also override the file

WRITING AND APPENDING TO FILES {WWW}
it overrides the file, all the info will be deleted and new info is added on
the user can also create a new file by using this function

-SO THE USER CAN OVERRIDE A FILE, CREATE A NEW FILE AND /OR APPEND INFO ON THE EXISTING FILE """


try:

    number = int(input('Enter a number'))
    print(number)
    print(10/0)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('Invalid input')
    

#########################    READING FILES   #####################
aws_certs = open('aws_certs.txt', 'r')
print(aws_certs.readable())
print(aws_certs.read())
# print(aws_certs.readline()[])
print(aws_certs.readlines())

for cert in aws_certs.readlines():
    print(cert)
aws_certs.close()

#################### WRITING TO FILES#####################################

################ A #######################################################
aws_certs = open('aws_certs.txt', 'a')
aws_certs.write("Lenny  - Solutions Architect")
aws_certs.write("\nLinda  - DevOps Engineer")

aws_certs.close()
################ W #######################################################
aws_certs = open('aws_certs.txt', 'w')

aws_certs.write("Linda  - DevOps Engineer")
# Linda overrides the file info
aws_certs.close()
########### W NEW FILE
aws_certs = open('aws_certs.txt', 'w')
# creates another file with the same info as the original file
aws_certs.write("Linda  - DevOps Engineer")
# Linda overrides the file info
aws_certs.close()

