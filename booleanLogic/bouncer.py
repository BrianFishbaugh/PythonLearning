#PseudoCode

#Ask For Age
age = input("How Old Are You? ")
if age:
	age = int(age)
	if age >= 18 and age < 21:
		print("Enter, But you Need A Wristband")
	elif age >= 21:
		print("You're good to enter and can drink")
	else:
		print("Why're you here, you're too young")
else: 
	print("Please Enter An Age")
	