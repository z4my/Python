print ("hello world")
name = "Sumit"
age = 20
height = 5.8

print(name)
print(age)
print(height)

print("My name is: ", name)
print("My age is: ", age)
print("My height is: ", height)
print("My name is: " + name)
print("My age is: " + str(age))#to convert int to string 

print(f"My name is {name}, and My age is {age} and My height is {height}")

print(type(name))
print(type(age))
print(type(height))

print(type(str(age)))
print(str(age))#to convert int to string
print(type(int(height)))
print(int(height))#to convert float to int
print(type(float(age)))
print(float(age))#to convert int to float
print(type(bool(age)))
print(bool(age))#to convert int to bool
print(type(bool(name)))
print(bool(name))#to convert string to bool
print(type(bool(height)))
print(bool(height))#to convert float to bool

old= False
print(type(old))
print(old)

z= None
print(type(z))
print(z)#none

#To print sum of two numbers
num1 = 10
num2 = 20
sum = num1 + num2
print("Sum of two numbers is: ", sum)
#To print difference of two numbers
diff = num1 - num2
print("Difference of two numbers is: ", diff)
#To print product of two numbers
product = num1 * num2
print("Product of two numbers is: ", product)
#To print quotient of two numbers
quotient = num1 / num2
print("Quotient of two numbers is: ", quotient)
#To print remainder of two numbers
remainder = num1 % num2
print("Remainder of two numbers is: ", remainder)
#To print power of two numbers
power = num1 ** num2
print("Power of two numbers is: ", power)
#To print floor division of two numbers
floor_division = num1 // num2
print("Floor division of two numbers is: ", floor_division)
#To print average of two numbers
average = (num1 + num2) / 2
print("Average of two numbers is: ", average)
#To print maximum of two numbers
max = num1 if num1 > num2 else num2
print("Maximum of two numbers is: ", max)
#To print minimum of two numbers
min = num1 if num1 < num2 else num2
print("Minimum of two numbers is: ", min)
#To print square of a number
square = num1 * num1
print("Square of a number is: ", square)
#To print cube of a number
cube = num1 * num1 * num1
print("Cube of a number is: ", cube)
#To print square root of a number
import math
square_root = math.sqrt(num1)
print("Square root of a number is: ", square_root)
#To print cube root of a number
cube_root = num1 ** (1/3)
print("Cube root of a number is: ", cube_root)
#To print factorial of a number
factorial = math.factorial(num1)
print("Factorial of a number is: ", factorial)
#To print logarithm of a number
logarithm = math.log(num1)
print("Logarithm of a number is: ", logarithm)
#To print exponential of a number
exponential = math.exp(num1)
print("Exponential of a number is: ", exponential)
#To print sine of a number
sine = math.sin(num1)
print("Sine of a number is: ", sine)
#To print cosine of a number
cosine = math.cos(num1)
print("Cosine of a number is: ", cosine)
#To print tangent of a number
tangent = math.tan(num1)
print("Tangent of a number is: ", tangent)
#To print degree of a number
degree = math.degrees(num1)
print("Degree of a number is: ", degree)
#To print radian of a number
radian = math.radians(num1)
print("Radian of a number is: ", radian)
#To print absolute value of a number
absolute_value = abs(num1)
print("Absolute value of a number is: ", absolute_value)
#To print round off value of a number
round_off = round(num1)
print("Round off value of a number is: ", round_off)
#To print floor value of a number
floor_value = math.floor(num1)
print("Floor value of a number is: ", floor_value)
#To print ceil value of a number
ceil_value = math.ceil(num1)
print("Ceil value of a number is: ", ceil_value)

#Differet type of operators in python
a= 5
b= 2

#Arithmetic operators
# +, -, *, /, %, **, //
# + : addition
# - : subtraction
# * : multiplication
# / : division
# % : modulus
# ** : exponentiation
# // : floor division
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a % b) # modulus
print(a ** b) # exponentiation
print(a // b) # floor division


#Assignment operators
# =, +=, -=, *=, /=, %=, **=, //=
# = : assignment
# += : addition assignment
# -= : subtraction assignment
# *= : multiplication assignment
# /= : division assignment
# %= : modulus assignment
# **= : exponentiation assignment
# //= : floor division assignment

#Comparison operators
# ==, !=, >, <, >=, <=
# == : equal to
# != : not equal to
# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to

#Logical operators
# and, or, not  
# and : logical and
# or : logical or
# not : logical not

#Identity operators
# is, is not
# is : identity
# is not : not identity

#Membership operators
# in, not in
# in : membership
# not in : not membership

#Bitwise operators
# &, |, ^, ~, <<, >>
# & : bitwise and
# | : bitwise or
# ^ : bitwise xor
# ~ : bitwise not
# << : left shift
# >> : right shift

#Ternary operator
# (condition) ? (true value) : (false value)