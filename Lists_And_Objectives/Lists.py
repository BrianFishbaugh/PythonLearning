tasks = ["Install Python", "Learn Python", "Take a Break"]

print(tasks)

task1 = "Install Python"
task2 = "Learn Python"
task3 = "Take a Break"

list_Of_tasks = [task1 , task2 , task3]

print(list_Of_tasks)

print(len(list_Of_tasks))

print("Install Python" in list_Of_tasks)
print(2 in list_Of_tasks)

colors = ["Purple" , "Teal" , "Orange" , "Blue" , "Green" , "Yellow" , "Doesn't Really Matter What I Type Here, this is just practice " , "Green" , True, 9.0 , 2 , "jjj"]

for col in colors:
	print(col)


numbers = [4 , 6 , 2 , 8 , 9 , 10 , 7]

for num in numbers:
	print(num * num) 


i = 0

while i < len(numbers):
	print(numbers[i] * numbers[i])
	i += 1


nums = [1 , 2 , 3]
nums.append("x")
print(nums)

nums.insert( 2 , 5)
print(nums)

nums.pop()
print(nums)

nums.pop(0)
print(nums)

nums.remove(3)
print(nums)

nums.clear()
print(nums)