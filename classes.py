import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        # Make sure to set this to a random amount of damage, ideally based on attack power. randit()
        random_int = random.randint(-5, 5)
        self.attack_power += random_int
        damage = self.attack_power

        # Check if the opponent has a 'avoidAttack' attribute. If they do not, proceed with the attack.
        if not hasattr(opponent, 'avoidAttack'):
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!") 
        elif hasattr(opponent, 'avoidAttack') and opponent.avoidAttack == False: # Else, if they do have an 'avoidAttack' attribute and the value is False, proceed with the attack.
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        elif hasattr(opponent, 'avoidAttack') and opponent.avoidAttack == True: # Else, if they do have an 'avoidAttack' attribute and the value is True, set the value False and display that the attack was evaded.
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.avoidAttack = False

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
                              
    def heal(self):
        self.health += 20
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"\n{self.name} healed for 20 health! {self.name} health total: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.avoidAttack = False

    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Rush Attack") # Increases own damage by 15 and attacks
        print("2. Strike and Heal") # strikes the opponent and heals for half of the damage dealt

        action = input("Which special ability do you want to use? ")
        
        if action == '1':
            self.attack_power += 15
            opponent.health -= self.attack_power
            print(f"\n{self.name} is using the Rush Attack to increase their damage to {self.attack_power}.")
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        elif action == '2':
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2 # floor division rounds to the nearest integer

            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} used the Strike and Heal to attack {opponent.name} for {self.attack_power} damage and healed back to {self.health} Health")
        else:
            print ("\nInvalid selection, please try again!")
            return self.special_ability(opponent)

        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.avoidAttack = False
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Sorcery Calling") # increases attack power but does not attack
        print("2. Ambush") # strikes the opponent for half damage and evades next attack
        action = input("Which special ability do you want to use? ")
        
        if action == '1':
            self.attack_power += 15
            print(f"\n{self.name} is using the Sorcery Calling to increase their damage to {self.attack_power}.")
        elif action == '2':
            opponent.health -= self.attack_power // 2            
            self.avoidAttack = True
            print(f"\n{self.name} ambushed {opponent.name} and damaged them for {self.attack_power}. He will also evade the next attack!")
        else:
            print ("\nInvalid selection, please try again!")
            return self.special_ability(opponent)
                        
# Create Archer class
class Archer(Character):
    def __init__(self, name, quick_shot=50):
        super().__init__(name, health=120, attack_power=25)
        self.quick_shot = quick_shot
        self.avoidAttack = False

        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Quickshot") # Attacks with double the damage
        print("2. Evade") # avoids the next attack
        action = input("Which special ability do you want to use? ")
        
        if action == '1':
            opponent.health -= self.quick_shot
            print(f"\n{self.name} used a double arrow attack that doubled their damaged to {self.quick_shot}.")
            print(f"{self.name} attacks {opponent.name} for {self.quick_shot} damage!")
        elif action == '2':
            self.avoidAttack = True
            print(f"\n{self.name} used Evade. He will evade the next attack!")
            print(f"\n{self.name} ambushed {opponent.name} and damaged them for {self.attack_power}. He will also evade the next attack!")
        else:
            print ("\nInvalid selection, please try again!")
            return self.special_ability(opponent)

                   
# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30)
        self.avoidAttack = False
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Holy Strike") # Increases own damage by 15 and attacks
        print("2. Divine Shield") # avoids the next attack
        action = input("Which special ability do you want to use? ")
        
        if action == '1':
            self.attack_power += 20
            opponent.health -= self.attack_power
            print(f"\n{self.name} is using the Holy Strike to increase their damage to {self.attack_power}.")
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        elif action == '2':
            self.avoidAttack = True
            print(f"\n{self.name} used Divine Shield. He will evade the next attack!")
            print(f"\n{self.name} ambushed {opponent.name} and damaged them for {self.attack_power}. He will also evade the next attack!")
        else:
            print ("\nInvalid selection, please try again!")
            return self.special_ability(opponent)
                    
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.avoidAttack = False

    def regenerate(self):
        self.health += 5
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")