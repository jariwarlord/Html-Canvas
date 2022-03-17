# a = "Sabri Erdem"
# if "i E" in a:
#     print("It is found in the text")
#     print(a[2:9])
#     print(a[5:-1])
#     print(a.upper())  
#     print(a.lower())
# b = "Sabri"
# print(a.replace("b","d"))
# a = b 
# a = a.replace("b","d")
# print(a)
# print(b)


# c = "Sabri"
# d = "Edrem"
# print(c," ",d)

# e = c + " " + d
# print (e)



a = "berke"
b = "dalar"
age = 22
print("My name is",a + b ,"My age is : " ,age)

myText = "My name is Sabri Erdem, and I am {}"
print(myText.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))