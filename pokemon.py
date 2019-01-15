import time
import random


print()
print('-'*55)
print()

print('A wild Blastoise appears!')
time.sleep(2)
print('...the music changes...')
time.sleep(2)
print('Charizard, I choose you!')
print()

Charizard_hp = 200
Blastoise_hp = 250

Charizard_hp = int(Charizard_hp)

a = ["(1) Flamethrower", "(2) Ignite", "(3) Overheat", "(4) Ember"]

time.sleep(0.5)

while Charizard_hp > 0 and Blastoise_hp > 0:

	print('What will Charizard do? Choose the number...')
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
		time.sleep(1.2)
		print('Blastoise lost 30 HP')
		print()
	elif player_move == 2:
		Charizard_hp = Charizard_hp + 25
		print('Charizard uses Ignite!')
		print()
		time.sleep(1.2)
		print('Charizard heals 25 health')
		print()
	elif player_move == 3:
		Blastoise_hp = Blastoise_hp - 20
		Charizard_hp = Charizard_hp - 10
		print('Charizard uses Overheat!')
		print()
		time.sleep(1.2)
		print('Its not very effective...')
		print()
		time.sleep(1.2)
		print('Blastoise lost 20 HP')
		print()
		time.sleep(1.2)
		print('Charizard is hurt by recoil... 10 HP')
		print()
	elif player_move == 4:
		Blastoise_hp = Blastoise_hp - 15
		print('Charizard uses Ember')
		print()
		time.sleep(1.2)
		print('Its not very effective...')
		print()
		time.sleep(1.2)
		print('Blastoise lost 10 HP')
		print()

	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		Charizard_hp = Charizard_hp - 100
		print('Blastoise uses Surf')
		print()
		time.sleep(1.2)
		print('Its super effective!')
		print()
		time.sleep(1.2)
		print('Charizard loses 100 HP')
		print()
	if enemy_move == 2:
		Charizard_hp == Charizard_hp - 120
		print('Blastoise uses Hydro Pump!')
		print()
		time.sleep(1.2)
		print('Its super effective!')
		print()
		time.sleep(1.2)
		print('Charizard loses 120 HP')
		print()


