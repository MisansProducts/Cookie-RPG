#Made by Alex

#======Libraries======
import random #For random selection and chance
import time #To make text output appear slower which causes less spam

#======Class Definitions======
#Player
class player:
	#Constructor initialization
	def __init__(self):
		#Variables
		self.maxHP = 100 #Maximum hit points (health)
		self.hp = self.maxHP #Current hit points (health)
		self.cookies = 0 #Cookies
		self.minDMG = 5 #Lowerbound on damage
		self.maxDMG = 15 #Upperbound on damage
		self.exp = 0 #Experience points
		self.maxEXP = 100 #Maximum experience points
		self.lvl = 1 #Current level
	#Fight
	def fight(self, enemyListIndex = 0):
		enemy = enemyList[enemyListIndex] #Gets the enemy from the enemy list
		print(f"You shot an arrow at {enemy.name}.")
		time.sleep(0.25)
		hit = random.randint(self.minDMG, self.maxDMG) #Amount of HP to take away
		print(f"{tab}Hit! -{hit} health")
		enemy.hp -= hit #Removes HP from enemy
		#Enemy is dead
		if enemy.hp <= 0:
			enemy.hp = 0
			cookiesGained = random.randint(5, 25) * self.lvl #Random amount of cookies rewarded
			expGained = random.randint(5, 25) * self.lvl #Random amount of exp rewarded
			self.cookies += cookiesGained
			self.exp += expGained
			print(f"{tab}{enemy.name} is dead!")
			print(f"{tab}{tab}+{cookiesGained} cookies")
			print(f"{tab}{tab}+{expGained} experience points")
			#Level up
			if self.exp >= self.maxEXP:
				self.exp = 0 #Resets experience points
				self.lvl += 1 #Increases level
				self.maxEXP += 50 #Increases max exp
				hpGained = random.randint(15, 50) #Random HP rewarded from level up
				self.hp += hpGained
				self.maxHP += hpGained
				self.minDMG += 10 #Increases min damage
				self.maxDMG += 15 #Increases max damage
				#Announces level up
				print(f"{tab}{tab}Level up!")
				print(f"{tab}{tab}{tab}Your maximum health increased! +{hpGained} health")
				print(f"{tab}{tab}{tab}+12.5 average attack")
			enemyList.pop(enemyListIndex) #Removes enemy from the enemy list
		#Enemy is alive
		else:
			print(f"{tab}{enemy.name} (Health: {enemy.hp}/{enemy.maxHP})")
			#Neutral enemies become hostile
			if enemy.behavior == "Neutral":
				enemy.behavior = "Hostile"
		#Enemies attack back
		for enemy in enemyList:
			#Hostile enemies attack
			if enemy.behavior == "Hostile":
				time.sleep(0.25)
				enemy.fight()
				#Game ends when player is dead
				if self.hp == 0:
					break

#Enemy
class enemy:
	#Constructor initialization
	def __init__(self):
		#Lists of names
		shorelineEnemies = (
			"Snake", "Poison Scorpion", "Scorpion Queen", "Pirate", "Piratess",
			"Bandit", "Bandit Leader", "Red Gelatinous Cube",
			"Purple Gelatinous Cube", "Green Gelatinous Cube"
		)
		lowlandsEnemies = (
			"Hobbit Mage", "Hobbit Rogue", "Hobbit Archer", "Elf Wizard",
			"Elf Archer", "Elf Swordsman", "Elf Mage", "Goblin Mage",
			"Goblin Rogue", "Goblin Warrior", "Bunny", "Giant Crab"
		)
		#List of the lists of names
		possibleNames = (
			shorelineEnemies, lowlandsEnemies
		)
		#List of behaviors
		behaviors = (
			"Hostile", "Neutral", "Passive"
		)
		#Each behavior has a different weight (respectively)
		behaviorWeights = (
			50, 30, 20
		)

		#Variables
		self.name = random.choice(random.choice(possibleNames))
		self.maxHP = int((random.randint(1, 75) / 100) * client.maxHP)
		self.hp = self.maxHP
		self.behavior = random.choices(behaviors, behaviorWeights)[0]
	#Fight (attack the player)
	def fight(self):
		hit = int((random.randint(1, 25) / 100) * client.maxHP) #Amount of HP to take away
		print(f"\n{self.name} attacks! -{hit} health")
		client.hp -= hit
		#Player is dead
		if client.hp <= 0:
			client.hp = 0
			return print(f"{tab}{self.name} killed you!\n")
		#Player is alive
		else:
			print(f"{tab}Your health: {client.hp}/{client.maxHP}")
	#Appear
	def appear(self):
		print(f"{self.name} appeared (Health: {self.hp}/{self.maxHP})")

#Commands
#List of commands: Help, stats, check, fight
class commands:
	#Variables
	global tab #Allows the scope of tabs to be used with the functions below
	tab = "    " #Formatting tabs to look nice
	
	#-=-=-= Help Command =-=-=-
	def help():
		print("Commands:")
		print(f"{tab}\"Help\" - Bring up this list of commands.")
		print(f"{tab}\"Stats\" - View your attributes.")
		print(f"{tab}\"Check\" - Take a good look at your enemies.")
		print(f"{tab}\"Fight\" - Attack your enemies.")
		print(f"{tab}\"Eat\" - Restore your health by eating cookies.")
	#-=-=-= Stats Command =-=-=-
	def stats(self):
		print("Attributes:")
		print(f"{tab}Level: {self.lvl} (Experience: {self.exp}/{self.maxEXP})")
		print(f"{tab}Health: {self.hp}/{self.maxHP}")
		print(f"{tab}Cookies: {self.cookies}")
		print(f"{tab}Attack: {self.minDMG} - {self.maxDMG}")
	#-=-=-= Check Command =-=-=-
	def check():
		print("Enemies:")
		for enemy in enemyList:
			time.sleep(0.25)
			print(f"{tab}{enemy.name} (Health: {enemy.hp}/{enemy.maxHP}) ({enemy.behavior})")
	#-=-=-= Fight Command =-=-=-
	def fight():
		#Single enemy
		if len(enemyList) == 1:
			client.fight()
		#Multiple enemies
		else:
			print("Who do you want to attack?")
			for i in range(1, len(enemyList) + 1):
				time.sleep(0.25)
				enemy = enemyList[i - 1]
				print(f"{tab}{i}) {enemy.name} (Health: {enemy.hp}/{enemy.maxHP})")
			#Attempts to parse input
			try:
				time.sleep(0.25)
				response = int(input("\n>>Attack: "))

				#Range error
				if response < 1 or response > len(enemyList):
					raise ValueError
			#Returns on error
			except ValueError:
				return print("Unknown target.")
			#Attacks the selected enemy
			else:
				client.fight(response - 1)
	#-=-=-= Eat Command =-=-=-
	def eat():
		#Prompt
		print("How many cookies do you want to eat?")
		print(f"{tab}Cookies: {client.cookies}")
		#Attempts to parse input
		try:
			response = int(input("\n>>Amount: "))

			#Range error
			if response < 1:
				raise Exception(f"You can't eat {response} cookies!")
			elif response > client.cookies:
				raise Exception("You don't have that many cookies.")
		#Error handling (general)
		except ValueError:
			return print("Unknown amount of cookies.")
		#Error handling (range)
		except Exception as rangeError:
			return print(rangeError)
		#Eats cookies
		else:
			#Calculates amount of cookies eaten
			hpGained = response
			newHP = client.hp + hpGained #New health (supposedly)
			#Checks for range error
			if newHP >= client.maxHP:
				hpGained -= (newHP - client.maxHP) #Recalculates health gain
			client.cookies -= hpGained #Removes cookies
			client.hp += hpGained #Adds health
			#No difference
			if hpGained == 0:
				print("You don't feel very hungry.")
			#Ate some but not all cookies
			elif hpGained != response:
				print(f"You managed to eat {hpGained} cookies. +{hpGained} health")
				print(f"{tab}Cookies: {client.cookies}")
				print(f"{tab}Your health: {client.hp}/{client.maxHP}")
			#Ate all the cookies
			else:
				print(f"You ate {hpGained} cookies! +{hpGained} health")
				print(f"{tab}Cookies: {client.cookies}")
				print(f"{tab}Your health: {client.hp}/{client.maxHP}")
			#Enemies attack
			for enemy in enemyList:
				#Hostile enemies attack
				if enemy.behavior == "Hostile":
					time.sleep(0.25)
					enemy.fight()
					#Game ends when player is dead
					if client.hp == 0:
						break

#Game Loop Definition
def gameLoop():
	time.sleep(0.25)

	#Prompt user input
	response = input("\n>>What will you do?: ")
	response = response.lower() #Convert to lowercase

	#-=-=-= Options =-=-=-
	#Help
	if response == "help":
		commands.help()
	#Stats
	elif response == "stats":
		commands.stats(client)
	#Check
	elif response == "check":
		commands.check()
	#Fight
	elif response == "fight":
		commands.fight()
	#Eat
	elif response == "eat":
		commands.eat()
	#Error
	else:
		print("Unknown command, type \"help\" for a list of commands.")

	#Player is dead
	if client.hp == 0:
		return False
	#Player is alive
	else:
		return True


#Run the game
if __name__ == "__main__":
	#Variables
	gameState = True
	presence = False #Enemy presence
	MAX_ENEMIES = 1 #Maximum amount of enemies allowed
	enemyList = [] #Stores a list of enemies

	#Introduction
	print("Welcome to Cookie RPG!")
	print("By: Alex Akoopie")
	print("Beta Tester: Zhiwen Zhen\n")
	time.sleep(0.25)

	client = player() #Creates player object
	commands.help() #Introduces a list of commands

	#Main game loop
	while True:
		#Spawns enemies
		if not presence:
			presence = True #Sets presence to true; avoids multiple triggers
			MAX_ENEMIES = client.lvl #Maximum amount of enemies corresponds to level
			enemyIndex = 0 #Specific index in the enemy list (cannot be i since random chance causes it to skip some numbers)
			print() #Spacing
			for i in range(MAX_ENEMIES):
				#Chances of spawning more enemies decreases
				if random.randint(0, 100) >= 100 * (i/MAX_ENEMIES):
					enemyList.append(enemy()) #Creates enemy object in enemy list
					time.sleep(0.25)
					enemyList[enemyIndex].appear() #Alerts player that new enemy exist
					enemyIndex += 1

		#Game loop sequence
		if not gameLoop():
			break #Ends the game

		#Checks if the list of enemies is empty
		if not enemyList:
			presence = False #Resets enemy presence flag to spawn more enemies
	
	#Game over screen
	print("Game over.")