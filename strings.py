text = "hello world"

print(text.count('o'))
if text.startswith('hell'):
    print("It's hell in there")

if text.isalpha():
    print("String is all alpha")
else:
    print("String is not alpha")
#alpha is short for alphabet because there is a space, it is not alpha

if text.islower():
    print('string is lowercase')

text2 = ' \t\r\n'
if text2.isspace():
    print('string is whitespace')

if text2.isdigit():
        print('string is digit')

name = " Michelle"
age = 21
print("my name is{} and I am {} years old".format(name, age))

var1 = 01.05210002
var2 = 3
var3 = 1234236

#need walk through to understand better
print("text{0:5.3f}text{1:3d}text{2:f}".format(var1, var2, var3))


