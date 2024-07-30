#Write a Python program to calculate the length of a string.

"""METHOD 01"""
#Taking Input from User

var=input("Enter the String: ")
print(len(var))

"""METHOD 02"""
count=0
for ele in var:
    count +=1
print(count)