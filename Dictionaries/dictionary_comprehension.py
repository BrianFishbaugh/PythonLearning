#SYNTAX
##  {___ : ____ FOR ____ IN ____ }
#Iterates over Keys by defaults

numbers = dict(first = 1 , second = 2 , third = 3)

squared_numbers = {key : value ** 2 for key, value in numbers.items()}

print(squared_numbers)

print({num : num * 2 for num in [1 , 2 , 3, 4 , 5]})

str1 = "ABC"
str2 = "123"
combo = {str1[i] : str2[i] for i in range(0 , len(str1))}

print(combo)

user = {
	'name' : 'Brian' , 
	'city' : 'Columbus' , 
	'color' : 'Orange'	
}

yelling_user = {k.upper() : v.upper() for k,v in user.items()}
print(yelling_user)


#Conditional Logic with Dictionaries

num_list = [1 , 2 , 3 , 4]

num_dict = { num : ("even" if num % 2 == 0 else "odd") for num in range(1,10000) }

print(num_dict)