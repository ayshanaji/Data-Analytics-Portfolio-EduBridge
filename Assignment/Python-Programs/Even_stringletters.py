word= input("enter a word : ")
print("the original string:",word)
x=list(word)
for i in x[0::2]:
    print(i)
