"""
Write a  Python program that takes a string and replaces all the characters with their respective numbers.
"""

strng="content"
def a():
    return " ".join(str(ord(i)-96) for i in strng.lower() if i.isalpha())
z=a
print(z)
for i in strng.lower():
    a=ord(i)-96
    print(a)
