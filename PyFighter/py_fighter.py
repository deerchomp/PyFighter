#Py Fighter
#TODO:
#fix reroll function
#add combat engine
#modify name function to include dictionaries

import random

class Fighter:
    def __init__(self):
        self.strength = random.randint(0,15)
        self.intel = random.randint(0,15)
        self.agi = random.randint(0,15)
        self.vita = random.randint(0,15)

    def mainAttrib(self):
        random_attribute = random.randint(1,3)
        if random_attribute == 1:
            self.random_attribute = 'Strength'
            self.strength += random.randint(0,5)
        if random_attribute == 2:
            self.random_attribute = 'Agility'
            self.agi += random.randint(0,5)
        if random_attribute == 3:
            self.random_attribute = 'Intelligence'
            self.intel += random.randint(0,5)

    def fighterWeapon(self):
        self.weapon = random.randint(1,3)
        if self.weapon == 1:
            self.strength += 5
            self.weapon = 'Berserker Axe'
        if self.weapon == 2:
            self.agi += 5
            self.weapon = "Gladiator Sword"
        if self.weapon == 3:
            self.intel += 5
            self.weapon = "Mysterious Orb"

    def fighterStats(self):
        self.health_points = self.vita * 5 + 60
        self.attack_damage = self.strength * 1.5
        self.dodge_chance = self.agi * 1.5
        if self.agi > 15:
            self.critical_chance = self.agi * 2
        else:
            self.cticial_chance = 0.1

    def printStats(self):
        print()
        print()
        print(self.first + ' ' + self.last)
        print("-----------------------------")
        print("Main attribute: %s" % self.random_attribute)
        print("Weapon of choice: %s" % self.weapon)
        print("Strength: ",self.strength)
        print("Intelligence: ",self.intel)
        print("Agility: ",self.agi)
        print("Life: ",self.health_points)
        print("Average damage: ",self.attack_damage)
        print("Dodge chance: ",self.dodge_chance)

class Monster(Fighter):
    def __init__(self):
        Fighter.__init__(self)

    def nameMyMonster(self):
       self.first = random.randint(0,5)
       self.last = random.randint(0,5)
       if self.first == 0:
           self.first = "Samuel"
       if self.first == 1:
           self.first = "Greggory"
       if self.first == 2:
           self.first = "Grognar"
       if self.first == 3:
           self.first = "Loknar"
       if self.first == 4:
           self.first = "The"
       if self.first == 5:
           self.first = "El"

       if self.last == 0:
           self.last = "Deathblow"
       if self.last == 1:
           self.last = "Pwnkins"
       if self.last == 2:
           self.last = "Manslayer"
       if self.last == 3:
           self.last = "McCrucifier"
       if self.last == 4:
           self.last = "Blooddrinker"
       if self.last == 5:
           self.last = "Prime"

class Hero(Fighter):
    def __init__(self):
        Fighter.__init__(self)

    def nameMyHero(self):
        self.first = random.randint(0,5)
        self.last = random.randint(0,5)
        if self.first == 0:
            self.first = "Neo"
        if self.first == 1:
            self.first = "Sir"
        if self.first == 2:
            self.first = "Loktar"
        if self.first == 3:
            self.first = "Achilles"
        if self.first == 4:
            self.first = "Christian"
        if self.first == 5:
            self.first = "Conan"

        if self.last == 0:
            self.last = "The Barbarian"
        if self.last == 1:
            self.last = "Dragonkin"
        if self.last == 2:
            self.last = "Redwolf"
        if self.last == 3:
            self.last = "McDonald"
        if self.last == 4:
            self.last = "the Brave"
        if self.last == 5:
            self.last = "of Nazareth"

def giveRules():
    query = input("Create a character and fight against a computer controlled monster \n Would you like to play? y/n\n")
    play = bool(query)
    if query == 'y' or 'Y' or 'yes':
        return True
    else:
        return False
    return play

#reroll fighters seems sloppy and still broken
def rerollFighters(hero, monster):
    print()
    myquery = input("Would you like to reroll the combatants? y/n\n")
    while myquery == 'y' or 'Y' or 'yes':
        whichFighter = int(input("Which fighter would you like to reroll? \n 1. %s \n 2. %s \n 3. Both fighters \n 4. Do not reroll\n" % (hero.last, monster.last)))
        if whichFighter == 1:
            satisfied = 'n'
            while satisfied == 'n':
                hero = Hero()
                hero.mainAttrib()
                hero.fighterWeapon()
                hero.fighterStats()
                hero.nameMyHero()
                hero.printStats()
                print()
                satisfied = input("Is this your hero? y/n: ")
                if satisfied == 'y':
                    myquery = 'n'
                if satisfied == 'n':
                    print("=======================================")
            
        if whichFighter == 2:
            satisfied = 'n'
            while satisfied == 'n':
                monster = Monster()
                monster.mainAttrib()
                monster.fighterWeapon()
                monster.fighterStats()
                monster.nameMyMonster()
                monster.printStats
                print()
                satisfied = input("Is this your opponent? y/n: ")
                if satisfied == 'y':
                    myquery = 'n'
                if satisfied == 'n':
                    print("=======================================")
                
            
        if whichFighter == 3:
            satisfied = 'n'
            while satisfied == 'n':
                hero = Hero()
                hero.mainAttrib()
                hero.fighterWeapon()
                hero.fighterStats()
                hero.nameMyHero()
                monster = Monster()
                monster.mainAttrib()
                monster.fighterWeapon()
                monster.fighterStats()
                monster.nameMyMonster()
                hero.printStats()
                print('\nvs.\n')
                monster.printStats()
                satisfied = input("Is this compatible? y/n: ")
                if satisfied == 'y':
                    myquery = 'n'
                if satisfied == 'n':
                    print("=======================================")

        if whichFighter == 4:
            myquery = 7

        else:
            print("Input not recognized! Try again!")
            myquery = 'n'
            
def acceptBattle(monster):
    print()
    print('%s %s just called you out! Do battle!?' % (monster.first, monster.last))
    battlechoice = int(input("1. Come at me bro.\n2. You're not worth my time.\n\n"))
    if battlechoice == 1:
        combatEngine()
    else:
        print("You escaped successfully")

def coinFlip():
    coin_flip = input("Coin flip will decide who attacks first! Please select heads or tails.\n")
    coin_flip_result = random.randint(1,2)
    user_goes_first = True
    if coin_flip_result == 1:
        print("The result was heads")
    elif coin_flip_result == 2:
        print("The result was tails")
    
    if coin_flip == 'heads' and coin_flip_result == 1:
        print("You won the toss")
    if coin_flip == 'tails' and coin_flip_result == 2:
        print("You won the toss")
    else:
        print("You lost the toss")
        user_goes_first = False

    return user_goes_first
        
def combatEngine(hero, monster):
    print("Begin battle!")
    hero.printStats()
    print('\nvs.\n')
    monster.printStats()
    user_attacks = True
    while user_turn == True:
        choice = int(input("Select ability\n 1. Attack \n 2. Heal \n"))
        
        if choice == 1:
            monster.health_points - hero.attack_damage
            damage_dealt = monster.health_points - hero.attack_damage
            print("You did %f damage to %s" % (damage_dealt, monster.last))
            user_turn = False
            
        if choice == 2:
            hero.health_points += hero.intel * random.randint(.50,.85)
            healed_for = hero.health_points + hero.intel *  random.randint(.50,.85)
            print("You healed for %f" % (healed_for))
            user_turn = False

    while user_turn == False:
        monster_decision = random.randint(1,2)
        if monster_decision == 1:
            hero.health_points -= monster.attack_damage
            mon_damage_dealt = hero.health_points - monster.attack_damage
            print("%s did %f damage to you" % (monster.last, mon_damage_dealt))
        if monster_decision == 2:
            monster.health_points += monster.intel
                  

    
def main():
    play = giveRules()
    if play == True:
    ######################instantiation of combatants
        hero = Hero()
        hero.mainAttrib()
        hero.fighterWeapon()
        hero.fighterStats()
        hero.nameMyHero()

        monster = Monster()
        monster.mainAttrib()
        monster.fighterWeapon()
        monster.fighterStats()
        monster.nameMyMonster()

        print()
        hero.printStats()
        print('\nvs.\n')
        monster.printStats()
        #rerollFighters(hero, monster)
    #####################
        user_goes_first = coinFlip()
        
        acceptBattle(monster)
main()
