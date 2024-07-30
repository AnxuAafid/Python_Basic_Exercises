import string
strin=input("Enter something")

for ele in string.punctuation:
    strin=strin.replace(ele, "")
print(strin)