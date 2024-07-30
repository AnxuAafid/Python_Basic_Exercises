"""
Write a Python program to remove repeated consecutive characters
and replace them with single letters and print a updated string.
"""

var=input("Enter word: ")
new=var[0]
for ele in var:

    if new[-1] != ele:
        new= new+ele
print(new)