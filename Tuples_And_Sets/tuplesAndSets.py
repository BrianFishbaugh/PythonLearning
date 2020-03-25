
##### TUPLES ######

numbers = (1 , 2 , 3 , 4)

#Immutable

alphabet = ('a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z')

#Tuples are Faster
#Tuples are Safer (Against Bugs) 


#Can be used as Valid Keys in Dictionaries --- Cannot Use Lists

locations = {
	(35.6895 , 39.6917) , "Tokyo Office",
	(40.7128 , 74.0060) , "New York Office", 
	(37.7749 , 122.4194) , "San Fransisco Office"
}

#Examples
#Months of the Year
#Accessed same as A List

#Can have repeat Data
nums = (1 , 2 , 3 , 3, 3) 

#Iterating over a Tuple

for numbers in numbers: 
	print(numbers)

for locations in locations: 
	print(locations) 

for nums in nums: 
	print(nums)


### SETS #### 
#Sets are like Mathematical Sets --> Group of Items that have no duplicates and no order
### --- Cannot access them via Index, because there isn't one
#Don't care about Keys, or duplicates

s = {1 , 4 , 5}
s = set{1 , 4 , 5}

tests = set{1 , 4 , 5, 6, 6, 5, 4, 3, 2, 1}
print(tests) ###### Prints {1 , 4 , 6 , 5 , 2 , 3} No repeats

## Looping 
for x in s: 
	print(x) 

## Common Use Case 
cities = ["Tokyo" , "New York" , "San Fransisco" , "Berlin" , "Shenhai" , "Boston" , "Little Rock" , "Tokyo" , "Tokyo" , "Little Rock" , "Boulder" , "Kansas City" , "San Fransisco" , "Florence" , "Kansas City" , "Berlin"]

print(set(cities))
print(list(set(cities)))

## OR 
print(len(set(cities)))

################################################# SET METHODS ##############################################

#Add
t = set{1 , 2 , 3}
t.add(4)
print(t)  
t.add(3)
print(t) 


# REMOVE --- Throws Error if Info isn't in there
t.remove(3)
print(t)

#Discard -- Removes, but doesn't throw Error
t.discard(3)
print(t)


#Copy
u = t.copy()
print(u)

#Clear
t.clear()
print(t)

math_students = set{"Matt" , "James" , "Mark" , "Luke" , "John" , "Peter"}
bio_students = set{"Barnabus" , "Luke" , "Paul" , "Matt" , "Peter" , "John-Mark"}

##UNTION
print(math_students | bio_students)

##INTERSECTIONS
print(math_students & bio_students) 


######## SET COMPREHENSION ######
v = {x**2 for x in range(10)}

print(v) 



