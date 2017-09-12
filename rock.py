#!/usr/bin/python

import random

chance = "rock-paper-scissors"
chanceR = chance.split("-")
x = 1
y = 0
z = 0

print "A person walks down the hall and when he comes upon you he challenges you to a rock paper scissors duel."
print "He says due to league rules once your eyes meet with a champs you must do battle."

while (x <= 3):
	your_choice = raw_input("Do you throw rock, paper, or scissors: ")
	random.shuffle(chanceR)
	champ_choice = chanceR.pop()
	if (your_choice == 'rock' and champ_choice == 'rock' or your_choice == 'paper' and champ_choice == 'paper' or your_choice == 'scissors' and champ_choice == 'scissors'):
		print "You throw %s and he throws %s." % (your_choice, champ_choice)
		print "You tie round %d. Score(you-champ): %d-%d" % (x, y, z)
		x += 1
	elif (your_choice == 'rock' and champ_choice == 'scissors' or your_choice == 'paper' and champ_choice == 'rock' or your_choice == 'scissors' and champ_choice == 'paper'):
		print "You throw %s and he throws %s." % (your_choice, champ_choice)
		y += 1
		print "You win round %d. Score(you-champ): %d-%d" % (x, y, z)
		x += 1
	elif (your_choice == 'rock' and champ_choice == 'paper' or your_choice == 'paper' and champ_choice == 'scissors' or your_choice == 'scissors' and champ_choice == 'rock'):
		print "You throw %s and he throws %s." % (your_choice, champ_choice)
		z += 1
		print "You lose round %d. Score(you-champ): %d-%d" % (x, y, z)
		x += 1
if (y > z):
	print "Congratulations you have bested me and earned your space in the list of great duelists."
	yourTitle = raw_input("What would you like your title to be in the records? ")
	f=open("Champions.txt", "a+")
	for i in range(1):
		f.write("Original Champion: Balrog the Great\n 2nd Champion: Freed the Conquerer\n 3rd Champion: Bastion the Invincible\n 4th Champion: Artoria Pendragon\n 5th Champion: %s" % yourTitle)
		f.close()
	print "You have been added to the great volume, called Champion.txt"
elif (y < z):
	print "You put up a good fight but in the end are no match for me."
	yourTitle = raw_input("What would you like your title to be in the loss record? ")
	f=open("Fallen.txt", "a+")
	for i in range(1):
		f.write("1st Fallen: Mr.Meeseeks\n 2nd Fallen: All Might\n 3rd Fallen: Gon Freecss\n 4th Fallen: Alpha Icarus\n 5th Fallen: %s" % yourTitle)
		f.close()
	print "You have been added to the volume of the fallen, AKA Fallen.txt"
elif (y == z):
	print "For me a draw equals a loss, you have proven yourself good sir."
        yourTitle = raw_input("What would you like your title to be in the list of victors? ")
        f=open("Victors.txt", "a+")
        for i in range(1):
                f.write("1st Victor: Rick Sanchez\n 2nd Victor: Izuku Midoriya\n 3rd Victor: Dirty Dan\n 4th Victor: Ted Mosby\n 5th Victor: %s" % yourTitle)
                f.close()
	print "You have been added to the tome of victors, AKA Victors.txt" 



