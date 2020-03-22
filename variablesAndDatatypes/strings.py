
#Basic Strings
name = 'Brian'
name2 = "Brian"

message = "Brian Says 'I am Hilarious'"

print(message)


#String Breaks
msg = "New \nLine"

print (msg) 

string = "\\"
print(string)


#Concatenation
string1 = "Your"
string2 = " Face"
print(string1 + string2)

string3 = " Loser"
print(string1 + string2 + string3)

username = "Brian"
string4 = "Welcome to the Game "
string5 = "..."

print (string4 + username + string5)

string6 = "Ice"
string6 += " Cream"

print(string6)

#F-Strings
x = 10
f_string = f"I've told you {x} times already"

print(f_string) 


#Indexing Strings
name = "Brian"
info = name[0]
info2 = name[3]

print(info + ", " + info2)


#Converting Data Types
float_var = 12.2122342
int_var = int(float_var)

print(int_var)

num = 12
x = float(num)

print(type(x))

print(int(999.112213123))

y = 8
z = str(y)

print(z)
