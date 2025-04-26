###CONDITIONAL STATEMENTS- They are used to perform different actions based on different conditions.
##if-elif-else statement- It is used to execute a block of code if the condition is true, and another block of code if the condition is false.

#Example 1: Traffic light system

#light=(input("Enter the traffic light color:"))
# if light== "red":
#     print("Stop")
# elif light== "green":
#     print("Go")
# elif light== "yellow":
#     print("Start your engine")
# else:
#     print("Wrong input")

#Example 2: Calculating the grade of a student based on marks

#marks= int(input("Enter your marks: "))

# if marks>= 90:
#     grade= "A"
# elif (marks>= 80 and marks< 90):
#     grade= "B"
# elif (marks>= 70 and marks< 80):
#     grade= "C"
# else:
#     grade= "D"
# print("Your grade is: ", grade)

#Example 3: Nesting if-else statement

# age= int(input("Enter your age: "))
# if age>= 18:
#      if age>= 21:
#             print("You are eligible to vote and drink")
#      else:
#             print("You are eligible to vote but not to drink")
# else:
#     print("You are not eligible to vote or drink")


#####Some questions for practice

##Q.1 Writa a python code to check if a number entered by the user is odd or even.

# num= int(input("Enter a number: "))
# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

##Q.2 Write a python code to find the greatest of 3 numbers entered by the user.

# num1= int(input("Enter first number: "))
# num2= int(input("Enter second number: "))
# num3= int(input("Enter third number: "))
# if num1>num2 and num1>num3:
#     print("The greatest number is: ", num1)
# elif num2>num1 and num2>num3:
#     print("The greatest number is: ", num2)
# elif num3>num1 and num3>num2:
#     print("The greatest number is: ", num3)
# else:
#     print("All numbers are equal")

##Q.3 Write a python code to check if a number is a multiple of 8 or not.

# num= int(input("Enter a number: "))
# if num%8==0:
#     print("The number is a multiple of 8")
# else:
#     print("The number is not a multiple of 8")
