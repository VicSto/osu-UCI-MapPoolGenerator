-----osu!UCI Map Pool Generator-----

NOTE: The Python Imaging Library (PIL) is necessary in order to run the shell build of MapPoolInterface.py.

The osu!UCI Map Pool Generator is a program that utilizes a randomization algorithm on a .csv file of maps containing the information:
Artist	Title	Difficulty	Link	Mod		Length		Star	Song Number (starts at 0)

where...

Artist:
	The name of the song artist 
	
Title:
	The name of the song title
	
Difficulty:
	The name of the map difficulty (E.g., "Easy", "Hard", "Collab", "Miki's Insane")
	
Link:
	The URL link to the map
	
Mod:
	The desired specification for this map during the competition. Mods are Double Time, Hard Rock, Hidden, None, Tiebreaker
	
Length:
	Length of the song
	
Star:
	The star count of the song
	
Song Number:
	For the program's convenience, provide the song number 0 up to max # of songs for each Mod. (E.g., Having 27 Double Time maps in pool, the song number will go from 0 to 26 before reverting to 0 for next mod)


Usage:
	
	To run the generator, run the MapPoolInterface.py program.
	
	
NOTE: IF YOU ACCIDENTALLY RUN THE PROGRAM, IT WILL SAVE A BACKUP THAT YOU CAN USE TO REVERT THE CHANGES.
	