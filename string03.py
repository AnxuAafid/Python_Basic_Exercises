"""write a Python program to get a string made of the first 2 and last 2 characters of a given string.
If the string length is less than 2, return the empty string instead."""
""" -----------        METHOD 1    ----------------"""
strn=input("Enter the input: ")
if len(strn)>2:
    print("{} + {} = {}".format(strn[:2], strn[-2:], strn[:2]+strn[-2:]))
else:
    print("length of string is less or equal to 2")
""" -----------------        METHOD 2    ----------------------------  """
if len(strn)>2:
    a=strn[:2]
    b=strn[-2:]
    c=a+b
    print(c)
else:
    print("length of string is less or equal to 2")