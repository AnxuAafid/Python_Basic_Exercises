"""
Write a Python program to get a string from a given string where all occurrences of its first char
have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

"""

strng=input("Enter the string: ")
ele=strng[0]
strng=strng.replace(ele,'$')
strng=ele+strng[1:]
print(strng)
