playlist = {
	"Playlist Title" : "My_Playlist" , 
	"Playlist Author" : "Brian Fishbaugh" , 
	"Song" : [
		{'title' : 'Good Old Days', 'artist' : ['Macklemore , Kesha'], 'duration' : 4.00} , 
		{'title' : 'Drug Dealer' , 'artist' : ['Macklemore , Ariana DeBoo'] , 'duration' : 3.55} , 
		{'title' : 'Fake ID' , 'artist' : ['Macklemore'] , 'duration' : 2.33} , 
		{'title' : "Ain't Gonna Die Tonight" , 'artist' : ['Macklemore' , 'Eric Nally'] , 'duration' : 3.45} , 
		{'title' : 'These Days' , 'artist' : ['Rudimental' , 'Jess Glynne' , 'Macklemore' , 'Dan Caplen'] , 'duration' : 3.30}
	],  
}

total_length = 0
for song in playlist['Song']: 
	total_length += song['duration']

print(total_length)

print(playlist)