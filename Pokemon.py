class Pokemon:
    def __init__(self, name, level, health, max_health, types, is_knocked_out=None):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = types
        self.is_knocked_out = is_knocked_out
        self.count = 0
    
    def __repr__(self):
        # Printing a pokemon will tell you its name, its type, its level and how much health it has remaining
        return "This level {level} {name} has {health} hit points remaining. They are a {type} type Pokemon".format(level = self.level, name = self.name, health=self.health, type = self.type)

    def lose_health(self, health_lost):
        self.health_lost = health_lost
        if (self.health - self.health_lost) >= 0:
            self.health = self.health - self.health_lost
            print(self.name + ' now has '+ str(self.health) + ' health')  
            return self.health
        if (self.health - self.health_lost) <= 0:
            self.health = self.health - self.health
            print(self.name + ' now has '+ str(self.health) + ' health')  
            return self.health
    
    def gain_health(self, health_gained):
        self.health_gained = health_gained
        previous_health = self.health
        if (self.health + self.health_gained) <= 100:
            self.health += self.health_gained
            print(self.name + ' now has '+ str(self.health) + ' health')
            print(self.name + ' has recovered from ' +  str(previous_health) + ' to ' +  str(self.health)) 
            return self.health
    

    def knock_out(self,other_pokemon):
        self.other_pokemon = Pokemon
        death = other_pokemon.health - other_pokemon.health
        print(other_pokemon.name + ' has beed killed ' + 'by ' +self.name)
        other_pokemon.is_knocked_out = True
        other_pokemon.health = death
        return other_pokemon.is_knocked_out

    def revive(self):
        revive = self.max_health - self.health
        self.health += revive
        print(self.name + ' has beed revived completely')
        return self.health

    
    def experience(self, count):
        if count < 3:
            return self.level
        if count >=3 and count <= 5:
            self.level += 2
            return self.level
        elif count >5 and count <= 9:
            self.level += 3
            return self.level
        elif count > 9 and count <=14:
            self.level += 5
            return self.level
        else:
            self.level +=7
            return self.level

    def evolve(self,evolve,count):
        self.evolve = evolve
        if count >= 5 and count <= 7:
            self.__class__ = Squirtle
            #self.name = Squirtle()
            #self.type = Squirtle.type
            #self.level = Squirtle.level
            #self.health = Squirtle.health
            #self.max_health = Squirtle.max_health
            print(self.name + ' has been successfully upgraded to Squirtle pokemon')
            return self.evolve 
        
        if count >= 8 and count <= 10:
            self.__class__ = Charmander
            print(self.name + ' has been successfully upgraded to Charmander pokemon')
            return self.evolve
     
        if count > 10: 
            self.__class__ = Bulbasaur
            print(self.name + ' has been successfully upgraded to Bulbasaur pokemon')
            return self.evolve
        else: 
            print('Not yet ready to evolve')
            return self.evolve

    def attack(self, other_pokemon):
        self.other_pokemon = Pokemon
        if self.is_knocked_out == True:
            print(self.name + ' needs to heal after the knockout')
        else:
            if (other_pokemon.is_knocked_out) == True:
                print ('The ' + other_pokemon.name + ' is already knocked out ')
            else:
                if self.type == 'Fire':
                    
                    if other_pokemon.type == "Grass":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 2 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                    if other_pokemon.type == "Water":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 0.5 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                    if other_pokemon.type == "Fire":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 0.5 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                if self.type == 'Grass':
                    
                    if other_pokemon.type == "Fire":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 0.5 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his healh')
                            return other_pokemon.lose_health(damage)
                    
                    if other_pokemon.type == "Water":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 2 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                    if other_pokemon.type == "Grass":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 0.5 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)

                
                if self.type == 'Water':

                    if other_pokemon.type == "Fire":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 2 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                    if other_pokemon.type == "Grass":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 0.5 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                    if other_pokemon.type == "Water":
                        self.count +=1
                        count = self.count
                        self.level = self.experience(count)
                        if other_pokemon.set_block == True:
                            damage = 0.5* self.level *0.1
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage)
                        else:    
                            damage = 0.5 * self.level
                            print(self.name + ' attacked the '+ other_pokemon.name +' and has taken ' +str(damage) + ' from his fucking healh')
                            return other_pokemon.lose_health(damage) 
       


class Trainer:

    def __init__(self, pokemons, potions, name, current_pokemon):
        self.pokemons = pokemons
        self.potions = potions
        self.name = name
        self.current_pokemon = current_pokemon
        self.my_active_pokemon = self.pokemons[self.current_pokemon]

    def attack_other_trainer(self, other_trainer):
        try:
            their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
            return self.pokemons[self.current_pokemon].attack(their_pokemon)
        except IndexError:
            print("You've selected a Pokemon that doesn't exist")
            
            #print({a} + ' attacked ' + {b}.format(a=self.pokemons[self.current_pokemon],b = their_pokemon))
            #print({self.pokemons[self.current_pokemon]+ ' attacked ' + their_pokemon})
            #print('a' + ' attacked ' + 'b' )
        
        

    def potion_heal(self):
        gain = self.potions + self.my_active_pokemon.health
        if gain <= 100:
            return self.my_active_pokemon.gain_health(self.potions) 
        else:
            print('your pokemon ' + 'hasn not been recovered ' + 'as is it too much to drink. ' + 'Please lower your potion')

    def switch_pokemon(self, switch):
        try:
            self.current_pokemon = switch
            self.my_active_pokemon = self.pokemons[self.current_pokemon]
            if self.my_active_pokemon.is_knocked_out == True:
                print('Please select another Pokemon or heal its health')
            else:
                self.my_active_pokemon = self.pokemons[self.current_pokemon]
                print('You has successfuly switched to ' + str(self.my_active_pokemon))
                return self.my_active_pokemon
        except IndexError:
            print("You've selected a Pokemon that doesn't exist")


class Charmander(Pokemon):
    def __init__(self,name,level,health,max_health,types,is_knocked_out=None,set_block=None):
        super().__init__(name,level,health,max_health,types,is_knocked_out=None)
        self.set_block = set_block

    def block_attack(self,set_block):
            self.set_block = set_block
            if self.set_block == True:
                self.set_block = True
                
class Squirtle(Pokemon):
    def __init__(self, name, level=20):
        #lst = ['Squirtle',level,100,100,'Fire']
        #i for i in range(len(lst))
        super().__init__('Squirtle',level,100,100,'Fire')

class Bulbasaur(Pokemon):
    def __init__(self, level=25):
        super().__init__('Bulbasaur',level,100,100,'Grass')


#creating charmanders

aa = Charmander('Iverson',15,100,100,'Water')
aa.block_attack(True)
                   

#creating pokemons & trainers
a = Pokemon('Mario',10, 80, 100,'Fire')
b = Pokemon('Sergio',8, 90, 100,'Grass')
c = Pokemon('Maorino',9, 90, 100,'Water') 
trainer_one = Trainer([a,b,c],3,"Alex",0)

d = Pokemon('Rodman',10, 80, 100,'Fire')
e = Pokemon('Scottie Pippen',7, 90, 100,'Grass')
f = Pokemon('Michael',12, 90, 100,'Water')
trainer_two = Trainer([d,e,f],10,"JJ",0) 

g = Pokemon('Mike',15,90,100,'Fire')
h = Pokemon('MJ',12,95,100,'Grass')
j = Pokemon('AI',10,80,100,'Water')
trainer_three = Trainer([g,h,j],5,'Be like Mike',1) 


##scenario pokemon b attacks Charmander aa with block turned on
#b.attack(aa) 
#print(aa.health)

#scenario evolve from Pokemon to Charmander
c.evolve(c,6)
print(type(c))
#b.attack(c)
#print(c.health)
#knockou method
#c.knock_out(a)
#c.knock_out(b)
#c.knock_out(d)
#c.knock_out(e)
#print(c.level) 
#f.knock_out(h)
#f.knock_out(j)

#attack method

#c.attack(a)
#c.attack(b)
#c.attack(c)
#c.attack(d)
#c.attack(g)
#c.attack(h)
#c.attack(j)
#print(c.level)


#print(d.is_knocked_out,a.is_knocked_out)

#trainer_one.switch_pokemon(2)
#trainer_two.switch_pokemon(1)
#trainer_one.attack_other_trainer(trainer_two)
#print(d.health)

#print(b.health)

#trainer_three.attack_other_trainer(trainer_two)
#trainer_two.potion_heal()
#print(trainer_three.switch_pokemon(0))

#trainer_two.attack_other_trainer(trainer_one)



#print(trainer_two.attack_other_trainer(trainer_one))

   





        








