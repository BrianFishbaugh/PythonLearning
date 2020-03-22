#Clear ==> Clears all keys and values

d = dict(a = 1 , b = 2 , c = 3)
print(d)

d.clear() 
print(d)

#Copy ==> Makes a Copy of a Dictionary
e = dict(a = 1 , b = 2 , c = 3)
print(e)

clone_e = e.copy()
print(clone_e)

#FromKeys ==> Usually Used to Create Default Classes / Users etc... 
a = {}.fromkeys("[a]" , [1 , 2 , 3 , 4 , 5])

print(a)

#get ==> Retrieves a Key in an object and return None instead of KeyError if the key doesn't exist

dictionary = dict(a=1 , b=2 , c=3)

print(dictionary['a'])
print(dictionary.get('a'))
print(dictionary.get('d'))

#pop ==> removes a single item corresponding to the key
d = dict(a = 1 , b = 2 , c = 3)
print(d)
d.pop('a')
print(d)


#popitems ==> removes random item from dictionary
d = dict(a = 1 , b = 2 , c = 3)
print(d)
d.popitem()
print(d)
d = dict(a = 1 , b = 2 , c = 3)
d.popitem()


#update ==> Updates Keys and values in a dictionary with another set of kvp
d = dict(a = 1 , b = 2 , c = 3)
print(d)

e = dict(d = 4)

e.update(d)
print(e)