#!/usr/bin/python

import random

enemies = {
 'dragon': 'Do you sneak around the dragon and steal some gold off the floor [1] or attempt to talk to the dragon and ask for directions out of the cave [2].',
 'swordsman': 'Do you sneak around the sleeping warrior [3] or use a knife on the ground to slit his throat [4].',
 'archer': 'Do you attempt to sneakily steal a map from the archer [5] or attempt to kill the archer with a rock on the ground [6].',
 'musketeer': 'Do you sneak around the sleeping gunman [7] or attempt to sprint past him [8].'
 }

print "You awaken to find yourself on a damp rock floor. Fear within you swells and you imagine a terrifying enemy..."
add_enemy = raw_input("What is this enemy you fear? ")
enemies[add_enemy] = 'With your worst nightmare sleeping in front of you, do you [9] sneak around the edge or [10] pick up one of the weapons on the floor and attempt to kill it.\n'
random_enemy = random.choice(list(enemies.keys()))

chance = "rock-paper-scissors"
chanceR = chance.split("-")
x = 1
y = 0
z = 0

print "A person walks down the hall and when he comes upon you he challenges you to a rock paper scissors duel."
print "He says due to league rules once your eyes meet with a champs you must do battle."

while (x <= 3):
	your_choice = raw_input("Do you throw rock, paper, or scissors: ")
	while (your_choice != 'rock' and your_choice != 'paper' and your_choice != 'scissors'):
		your_choice = raw_input("Please enter rock, paper, or scissors: ")
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
		f.write("\nOriginal Champion: Balrog the Great\n 2nd Champion: Freed the Conquerer\n 3rd Champion: Bastion the Invincible\n 4th Champion: Artoria Pendragon\n 5th Champion: %s" % yourTitle)
		f.close()
	print "You have been added to the great volume, called Champion.txt"
elif (y < z):
	print "You put up a good fight but in the end are no match for me."
	yourTitle = raw_input("What would you like your title to be in the loss record? ")
	f=open("Fallen.txt", "a+")
	for i in range(1):
		f.write("\n1st Fallen: Mr.Meeseeks\n 2nd Fallen: All Might\n 3rd Fallen: Gon Freecss\n 4th Fallen: Alpha Icarus\n 5th Fallen: %s" % yourTitle)
		f.close()
	print "You have been added to the volume of the fallen, AKA Fallen.txt"
elif (y == z):
	print "For me a draw equals a loss, you have proven yourself good sir."
        yourTitle = raw_input("What would you like your title to be in the list of victors? ")
        f=open("Victors.txt", "a+")
        for i in range(1):
                f.write("\n1st Victor: Rick Sanchez\n 2nd Victor: Izuku Midoriya\n 3rd Victor: Dirty Dan\n 4th Victor: Ted Mosby\n 5th Victor: %s" % yourTitle)
                f.close()
	print "You have been added to the tome of victors, AKA Victors.txt" 

print "You look around and see the tunnel extend behind and in front of you, enter [1] to go the path in front of you, [2] to go the path behind you."

path1 = int(raw_input("> "))

while (path1 != 1 and path1 != 2 ):
	print "Please enter [1] or [2]."
	path1 = int(raw_input("> "))
if path1 == 1:
	print "Going forwards you enter a large open spaced cavern in the middle is a sleeping %s.\n" % random_enemy
	print enemies[random_enemy]
	path2 = int(input("> "))
	while (random_enemy == 'dragon' and path2 != 1 and path2 != 2 or random_enemy == 'swordsman' and path2 != 3 and path2 != 4 or random_enemy == 'archer' and path2 != 5 and path2 != 6 or random_enemy == 'musketeer' and path2 != 7 and path2 != 8 or random_enemy != 'dragon' and random_enemy != 'swordsman' and random_enemy != 'archer' and random_enemy != 'musketeer' and path2 != 9 and path2 != 10):
        	print "Please one of the numbers used in your scenario for options."
        	path2 = int(input("> "))
	if path2 == 1:
		print "You make it past the dragon with your pilfered gold and come to a 3 way tunnel split."
		print "Do you go left [1], right [2], or center [3]."
		path3 = int(raw_input("> "))
		while (path3 != 1 and path3 != 2 and path3 != 3):
	     		 print "Please enter [1], [2], or [3]."
       			 path3 = int(raw_input("> "))
		if path3 == 1:
			print "Following the left tunnel you see a man ahead guarding a door, he approaches you."
			print "Do you bribe him with the gold you picked up [1] or attempt to fight him [2]."
			path4 = int(raw_input("> "))
	                while (path3 != 1 and path3 != 2):
                        	 print "Please enter [1] or [2]."
                        	 path1 = int(raw_input("> "))
			if path4 == 1:
				print "The guard takes the gold with a glimmer in his eyes and then steps aside."
				print "You go through the door and see sunlight, smiling you head towards home."
				print "Congrats You Lived. Ending 1/15"
			elif path4 == 2:
				print "You attempt tackle the guard but he easily swats you aside. Then he draws a sword and runs you through the chest."
				print "You Have Died. Ending 2/15"
		elif path3 == 2:
			print "Taking the path on the right you come to an open room, inside are 20 guards eating lunch. The closest ones draw there weapons and charge you, easily they end your life."
			print "You Have Died. Ending 3/15"
		elif path3 == 3:
			print "While taking the center path the floor suddenly gives out and you fall to the bottom of a pit where spikes await you."
			print "You Have Died. Ending 4/15"
	elif path2 == 2:
		print "You approach the dragon and he awakens, you then ask if he knows the way out of this cave and the dragon responds by moving slightly to reveal a tunnel underneath him."
		print "You take the path after thanking the dragon and come to an exit that leads to the outside world."
		print "Congrats you escaped. Ending 5/15"
	elif path2 == 3:
		print "You manage to sneak around the warrior and pick up a dagger on the way through."
		print "You come to a series of turns, do you go left[1], right[2], or center[3]? "

