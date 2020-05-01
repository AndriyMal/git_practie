
class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def calculate_bill(self, purchased_items):
    sum_ = 0
    self.purchased_items = purchased_items
    for i in purchased_items:
      sum_ += self.items[i]
    return sum_     
 

  def __repr__(self):
    return (self.name +" menu availbale from " + str(self.start_time) +" am to "+ str(self.end_time))

items_brunch = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}  

brunch = Menu('brunch',items_brunch,11,16)
#print(brunch)

purchased_brunch = ['pancakes', 'home fries', 'coffee']
#print(brunch.calculate_bill(purchased_brunch))
#------------------------------------------------
items_early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

purchased_early_bird = ['salumeria plate','mushroom ravioli (vegan)']
early_bird = Menu('early_bird',items_early_bird, 15,18)
#print(early_bird.calculate_bill(purchased_early_bird))

#-----------------------------------------------------
items_dinner = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

dinner = Menu('dinner',items_dinner, 17,23)

#-----------------------------------------------------
items_kids = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids = Menu('kids',items_kids,11, 21)

menus = [brunch, early_bird, dinner, kids]

  
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return self.address

  def available_menus(self,time):
    self.time = time
    list = []
    for i in range(len(self.menus)):
      if self.time>= menus[i].start_time  and self.time <= menus[i].end_time:
        list.append(self.menus[i])
    return list 
    
flagship_store = Franchise("1232 West End Road",menus)    

new_installment =  Franchise("12 East Mulberry Street", menus)
franchises = [flagship_store,new_installment]
print(new_installment.available_menus(17))


class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

Basta_Fazoolinc = Business("Basta Fazoolin' with my Heart", franchises)

arepas_menu =  {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}



arepas_place = Franchise("189 Fitzgerald Avenue",arepas_menu)
















