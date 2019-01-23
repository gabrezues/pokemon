import time
import random
import pygame

print()
print('-'*55)
print()

print('A wild Blastoise appears!')
time.sleep(2)
print('...the music changes...')
time.sleep(2)
print('Charizard, I choose you!')
print()

Charizard_hp = 170
Blastoise_hp = 170

Charizard_hp = int(Charizard_hp)

a = ["(1) Flamethrower", "(2) Ignite", "(3) Overheat", "(4) Ember", "(5) Capture", "(6) Run"]

time.sleep(0.5)

while Charizard_hp > 0 and Blastoise_hp > 0:

	print('What will Charizard do? Choose the number...')
	print()
	print(*a, sep = "\n")

	player_move = input('Choose attack ')
	player_move = int(player_move)

	if player_move == 1:
		Blastoise_hp = Blastoise_hp - 30
		print('Charizard uses Flamethrower!')
		print()
		time.sleep(1.2)
		print('Its not very effective...')
		print()
		time.sleep(1.3)
		print('Blastoise lost 30 HP')
		print()
	elif player_move == 2:
		Charizard_hp = Charizard_hp + 30
		print('Charizard uses Ignite!')
		print()
		time.sleep(1.4)
		print('Charizard heals 30 health')
		print()
	elif player_move == 3:
		Blastoise_hp = Blastoise_hp - 20
		Charizard_hp = Charizard_hp - 10
		print('Charizard uses Overheat!')
		print()
		time.sleep(1.5)
		print('Its not very effective...')
		print()
		time.sleep(1.6)
		print('Blastoise lost 20 HP')
		print()
		time.sleep(1.7)
		print('Charizard is hurt by recoil... 10 HP')
		print()
	elif player_move == 4:
		Blastoise_hp = Blastoise_hp - 15
		print('Charizard uses Ember')
		print()
		time.sleep(1.8)
		print('Its not very effective...')
		print()
		time.sleep(1.9)
		print('Blastoise lost 10 HP')
		print()
	elif player_move == 5:
		print('Pokeball thrown!')
		capture_roll = random.randint(0,170)
		time.sleep(.9)
		print()
		if capture_roll > Blastoise_hp:
			print('You have captured Blastoise')
			print()
			break
		else:
			print('The wild Blastoise has escaped')
			print()
	elif player_move == 6:
		flee = random.randint(1,2)
		if flee == 1:
			print('You failed to escape')
		else:
			print('You safely got away...')
			break

	time.sleep(.5)

	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		Charizard_hp = Charizard_hp - 50
		print('Blastoise uses Surf')
		print()
		time.sleep(2.0)
		print('Its super effective!')
		print()
		time.sleep(2.1)
		print('Charizard loses 50 HP')
		print()
	if enemy_move == 2:
		Charizard_hp = Charizard_hp - 60
		print('Blastoise uses Hydro Pump!')
		print()
		time.sleep(2.2)
		print('Its super effective!')
		print()
		time.sleep(2.3)
		print('Charizard loses 60 HP')
		print()

	#check and avoid negative HP
	if Charizard_hp < 0:
		Charizard_hp = 0
	
	if Blastoise_hp < 0:
		Blastoise_hp = 0

	time.sleep(0.7)
	print('Updated HP:')
	print('Charizard: ' + str(Charizard_hp))
	print('Blastoise: ' + str(Blastoise_hp))
	print()

if Charizard_hp > 0 and Blastoise_hp == 0:
	print('The wild Blastoise has fainted.')
if Blastoise_hp > 0 and Charizard_hp == 0:
	print('Charizard has fainted. You lose.')