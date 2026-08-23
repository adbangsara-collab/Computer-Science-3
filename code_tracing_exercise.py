#Bangsara, "Arje" Althea Jean D. || 9-Helium

# code 1
# - - -
#def greet_students(name, char):
#    for i in range(char):
#        print(name[i])

#name = input("Enter a Name : " )
#nChar = input("Enter any numeric number : ")
#nChar = int(nChar)
#greet_students(name, nChar)

# = = =

# a. If name is "Joseph The Dreamer" and nChar is 5, what will be the output of the code above and why?
# -> The output would be a spelling of 'Joseph The Dreamer' up until the 5th character. Because the first 5 letters of the phrase 'Joseph Th Dreamer' are J, o, s, e, p.

# b. Using the same name, and nChar is 20, what now is the output and why?
# -> The program would print out the entire phrase 'Joseph The Dreamer', but it would also return an error. Because 20 is outside of the range of spelling 'Joseph The Dreamer' which is less than 20 characters.

# c. If there is an error message encountered in letter b, how will you be able to modify the code so that the error message will not appear.
# -> Create an if-else statement to check if the nChar is within the range of 'Joseph The Dreamer'. If it doesn't be sure to return a message that tells the user to put the number within the range.

# = = =

def greet_students(name, nChar):
    for i in range(char):
        print(name[i])

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)

if nChar > len(name):
    print("Please enter a number within the range of the name length.")
else:
    greet_students(name, nChar)

# - - -

# code 2
# - - -
#def greet_students(name, nChar):
#    for i in range(nChar):
#        print(name[0 : nChar])


#name = input("Enter a Name: ")
#greet_students(name, len(name))

# = = =

# a. Find the syntax error and modify it. Please identify the error and what did you do to fix it?
# -> There is no syntax error

# b. The code should be able to display a given name as an inverted triangle, please fix the code in order for it to do that.
# - > Add '- i' to 'print(name[0 : nChar]) within the square brackets

# = = =

def greet_students(name, nChar):
    for i in range(nChar):
        print(name[0 : nChar - i])

name = input("Enter a Name: ")
greet_students(name, len(name))

# - - -

# code 3

# n = 0
# while n < 1 or n > 100:
#    n = input("Enter a number from 1 to 100: ")
#    n = int(n)

# print("Sum of all squared numbers is", sum_of_squared(n))

# a. You are tasked to create the needed function/s that will return the sum of all squared numbers from 1 to n.

def sum_of_squared(n):
   for i in range(1, n + 1):
       result = int(sum(range(1, n + 1)))

       return result


n = 0

while n < 1 or n > 100:
    n = input("Enter a number from 1 to 100: ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))

