text = "happy birthday"
text.count("a")
text.count("day")
x = "Happy Birthday"
x.lower()
x.upper()
# strings are an immutable data type
# can mutate strings with reassignment
x = x.lower()
x.capitalize()
## capitalizes first letter
x.title()
## capitalizes first letter of each word
x.islower()
## returns boolean
x.isupper()
x.istitle()
## also returns boolean
x.isalpha()
## if everything in x is a letter; also depends on whether string contains a space
## also returns boolean
x.isdigit()
## if everything in x is a number
## returns a boolean
y = "happybirthday123"
y.isalnum()
## if everything is a letter or a number
## returns true, but if there is punctuation, is false
x = "happy birthday"
x.index("birthday")
## returns 6; every letter of a string has its own addres (index); start counting from 0
## needs to be a substring or else errors out
x.find("birthday")
## returns index, but if substring doesnt exist, gives -1
# both are case sensitive
y = "0000000happybirthday000000"
y.strip("0")
y.lstrip("0")
y.rstrip("0")
## removes all 0's, can also go from either side
## leaving parentheses in strip empty --> removes all spaces
len(y)
## returns length of string
