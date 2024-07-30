"""
Write a Python function that takes a list of words and return the longest word and the length of the longest one.
"""

list=["How","are","You", "tell", "me", "Something", "New"]
"----------------------------- METHOD 1 ----------------------"
leng=0
word=list[0]
for ele in list:
    if len(ele)>leng:
        leng=len(ele)
        word=ele

print("The word '{}' is longest word of lengeth {}".format(word,leng))
"----------------------------- METHOD 2 ----------------------"
dict={}
for ele in list:
    keys=dict.keys()

    dict[ele]=len(ele)
print(dict)

"----------------------------- METHOD 2 ----------------------"
word=[]
for ele in list:
    word.append((len(ele),(ele)))
word.sort()
print(word[-1][1])