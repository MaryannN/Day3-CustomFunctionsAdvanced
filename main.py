'''
Morning Recap
'''

# This section is recapping what we have learned so far in the AM section with introduction to variables.

# def cost_disney(number_of_adults, number_of_children, number_of_days):
#   adult_cost = number_of_adults * 100
#   print("calculated adult cost at " + str(adult_cost))

#   child_cost = number_of_children * 90
#   print("calculated child cost at " + str(child_cost))
  
#   daily_cost = adult_cost + child_cost
#   total_cost = daily_cost * number_of_days
#   return total_cost
# print(cost_disney(1,2,2))

'''
Default
'''
# # This section is creating Default Arguments
# # default arguments allow us to have a function that will either take a user-provided parameter OR a substitute if they don't provide anything.


# def greet_player(name = "User"):
#   #Note to Self - how would this work with input if at all?
#   print("Welcome to the game, " + name + ".")
#   print("Your current level is 1.")

# greet_player("David") # Code if the user provides their name
# greet_player()  # Code if the user chooses not to provide their name

# # Questions
# # What is the default argument? - User
# # Which greeting will use the default argument? - the one that input no parameter

'''
Calling Varibles
'''

# This section is calling with variables


# def greet(player):
#   if player == "Octavia":
#     return "Welcome, agent Spencer. We're big fans."
#   else:
#     return "Welcome, " + player

# print(greet("Maryann"))
# print(greet("Octavia"))

'''
User Input
'''

# # Use a variable to collect and store user input
# name1 = input("Enter player 1's name: ") 

# # Pass in our `name1` variable as the argument for our greet function.
# print(greet(name1)) 

# name2 = input("Enter player 2's name")
# print(greet(name2))

'''
Scope
'''

# This section is called "Scope". Scope refers to the notion that variables are only accessible from inside the area where they are defined. In Python, there are two scopes:

# 1. Local scope refers to a variable defined from within a function. When variables are defined locally, they are only accessible from within that function. Trying to access them outside of a function, will render an error.
# Cant be seen by rest of program - can use keyword global to make it seen

# 2. Global scope refers to a variable defined in the main body of a Python script, outside of any function. Variables that are defined globally are accessible from anywhere in the code; they are available in both local and global scopes.
# Can be seen by rest of the program

# age = 15

# def have_a_birthday():
#   age = int(input("What is your age? "))
#   age += 1
#   print("Happy Birthday! You are now " + str(age))
#   return age
# ''''''

# have_a_birthday()

# # incremented age is outside birthday function so it stays 15 - can only refernce global variable
# print(age)

#Example of global condition

# age = 15

# def have_a_birthday():
#   global age
#   age= int(input("What is your age?"))
#   age += 1
#   print("Happy Birthday! You are now" + str(age))
#   return age

# have_a_birthday()

# print(age)


# # Default Argument
# def greet_player(name = "User"):
#   print("Welcome to the game, " + name + ".")
#   print("Your current level is 1.")

# greet_player("David") # Code if the user provides their name
# greet_player()  # Code if the user chooses not to provide their name





#Lab Reference
# Call the function
# def Leap_Year(year,regular):
#   if year % 4 ==0:
#     return True
#   else:
#     regular % 3 == 0
#     return False

# # Call the function
# print(Leap_Year(2024,2020))
