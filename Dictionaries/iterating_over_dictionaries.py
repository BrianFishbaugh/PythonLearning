User = {
	"Name" : "Brian" , 
	"Married" : True , 
	"IPA Lover" : True, 
	"Age" : 25,
	"address" : "3615 Beulah Circle"
}

for value in User.values():
	print(value)

for value in User.keys(): 
	print(value)

for value in User.items(): 
	print(value) 


for k,v in User.items(): 
	print(f"key is {k} and value is {v}")
