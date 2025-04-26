##ESCAPE SEQUENCE CHARACTERS

#Intro="Hi\nI am a python code generator."

#1.
#\n is used to create a new line in the string.
#print(Intro)

#2.
#\t is used to create a tab space in the string.
#print(Intro)


###STRING- String is a data type in python which is used to store a sequence of characters.
##Basic String Operations

#str1="Hi"
#str2="I am a python code generator."

#1. Concatenation- It is used to join two or more strings together.
#result=str1+" "+str2
#print(result)

#2. Length of a string- It is used to find the length of a string.
#result=str1+" "+str2
#length=len(result)
#print(length)

#3. Indexing- It is used to access the characters of a string using their index.
#result=str1+" "+str2
#length=len(result)
#first_character=result[0]#result[0] is used to get the first character of the string.
#last_character=result[length-1]#result[length-1] is used to get the last character of the string.
#print(first_character)
#print(last_character)

#4. Slicing- It is used to access a range of characters in a string using their index.
#result=str1+" "+str2
#First=result[0:2]#result[0:2],[:2] is used to get the first two characters of the string.
#Second=result[3:]#result[4:], [4:0] is used to get the string from 4th index to end of the string.
#print(First)
#print(Second)

##We can do slicing in reverse order also.
#result=str1+" "+str2
#First=result[-1]#result[-1] is used to get the last character of the string.
#Second=result[-10:-1]#result[-10:-1] is used to get the string from -2nd index to end of the string.
#print(First)
#print(Second)

####Some more string operations

#str="Hi I am a python code generator."
#1. Upper case- It is used to convert the string to upper case.
#result=str.upper()
#print(result)

#2. Lower case- It is used to convert the string to lower case.
#result=str.lower()
#print(result)

#3. Capitalize- It is used to convert the first character of the string to upper case.
#result=str.capitalize()
#print(result)

#4. Endswith- It is used to check if the string ends with the given string.
#result=str.endswith("generator.")
#print(result)

#5. Startswith- It is used to check if the string starts with the given string.
#result=str.startswith("Hi")
#print(result)

#6. Find- It is used to find the index of the given string in the string.
#result=str.find("python")
#print(result)

#7. Count- It is used to count the number of occurrences of the given string in the string.
#result=str.count("a")
#print(result)

#8. Replace- It is used to replace the given string with the new string in the string.
#result=str.replace("python","java")
#print(result)

###Some questions for practice

#Q.1 Write a python code to input user's name and print its length.
#name=input("Enter your name: ")
#length=len(name)
#print("Length of your name is: ",length)

#Q.2 Write a python code to find the occurrence of a character in a string.
#str=input("Enter a string: ")
#char=input("Enter a character: ")
#count=str.count(char)
#print("Occurrence of ",char," in ",str," is: ",count)  

