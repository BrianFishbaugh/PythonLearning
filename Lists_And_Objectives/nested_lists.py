nested_list = [[0 , 1 , 2] , [3 , 4 , 5] , [6 , 7 , 8]]
print(nested_list[0][1])

for x in nested_list:
	for val in x:
		print(val)

coords = [[10.423 , 9.132] , [37.212 , -14.092] , [21.367 , 32.572]]

for location in coords: 
	print(location)

for location in coords:
	for coord in location:
		print(coord)


#Nested List Comprehension

[[print(val) for val in l] for l in nested_list]

board = [[num for num in range(1,4)] for val in range(1 , 4)]
print(board)

print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])

print([["*" for x in range(1,4)] for i in range(1,4)])