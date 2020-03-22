#List Comprehension

#SYNTAX
numbers = [1 , 2 , 3 , 4]
doubled_numbers = []

for num in numbers: 
	doubled_number = num * num
	doubled_numbers.append(doubled_number)

print(doubled_numbers)

doubNum = [num * num for num in numbers]
print(doubNum)


name = 'brian'
newName = ''

newName = [char.upper() for char in name]
print(newName)

[number * 10 for number in range(1,6)]

x =[1 , 2 , 3 , 4 , 5]
string_x = [str(num) for num in x]

print(string_x)

colors = ['red' , 'orange' , 'yellow' , 'green' , 'blue' , 'indigo' , 'violet']
upper_color = []

upper_color = [color.upper() for color in colors]
print(upper_color)

color_edited = []
color_edited = [color + 's' for color in colors]

print(color_edited)


#List Comprehension with Conditional Logic

numbers = [1 , 2 , 3 , 4 , 5 , 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

wierdo = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]

print(evens)
print(odds)
print(wierdo)

with_vowels = 'This is so much fun!'
without_vowels = ''

without_vowels = ''.join(char for char in with_vowels if char not in "aeiou")

print(without_vowels)