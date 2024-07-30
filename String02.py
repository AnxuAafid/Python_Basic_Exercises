# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'

var=input("Enter the input: ")
dic={}

for ele in var:
    keys=dic.keys()
    if ele in keys:
        dic[ele] +=1
    else:
        dic[ele] = 1
print(dic)