"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing', replace 'ing', add 'ly' instead . If the string length of the given
string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

string=input("Enter the String: ")
if len(string)>2:
    if string[-3:]=="ing":
        #string=string.replace("ing","ly")--> this may replace all the ing as ly not the last one
        string=string[:len(string)-3]+"ly"
        print(string)
    else:
        string=string+"ing"
        print(string)

else:
    print("String Length is less than 3")
