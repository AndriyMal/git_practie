class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  
  def __repr__(self):
    return "{a}. '{t}'. {y}, {m}. {n}, {l}".format(a = self.artist, t = self.title, y = self.year, m = self.medium, n = self.owner.name, l = self.owner.location)


class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)


  def remove_listing(self, listing):
    self.listings.remove(listing)
  
  def show_listings(self):
    for i in self.listings:
      print(i)
      
veneer = Marketplace()

class Account:
    def __init__(self, account):
        self.account = account

    def add_money(self, amount_to_be_added):
        self.account += amount_to_be_added

    def deduct_money(self, amount_to_be_withdrawn):
        if self.account >= 0:
            self.account = self.account - amount_to_be_withdrawn
    
    def __repr__(self):
        return 'My account is {a}'.format(a=self.account)

class Marketplace_margin:
    def __init__(self,margin=30):
        if margin <=100:
            self.margin = margin

market_place = Account(0)
margin = Marketplace_margin(20)
Olga_account = Account(2500)
#edytta_account.add_money(350)
#print(Olga_account)
Oleg_account = Account(3000)
#moma_account.add_money(470)
#moma_account.deduct_money(700)
#print(Oleg_account)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    
    if self.is_museum == True:
      self.location = location
    else:
      self.location = "Private Collection"

  def sell_artwork(self, artwork, price,euros,premium):
    if artwork.owner == self:
       listing1 = Listing(artwork,price,self)
       veneer.add_listing(listing1)
       euros.account += (price - (premium.margin /100 * price))
  
  def buy_artwork(self, artwork,price,euros,premium):
      if artwork.owner != self:
        art_listing = 0
        for lst in veneer.listings:
         if lst.art == artwork:
             art_listing = lst
             lst.art.owner = self
             veneer.remove_listing(art_listing)
             euros.account = euros.account -  price
             market_place.account +=premium.margin/100 * price
             break



Oleg= Client("Oleg", "LA", True)


Olga = Client("Olga",None, False)

girl_with_mandolin = Art("Picasso, Pablo","Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, Olga)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '%s, %s. ' % (self.art.title,self.price)
    #{a} for {p}".format (a = self.art, p = self.price) 



Olga.sell_artwork(girl_with_mandolin,500,Olga_account,margin)
print(Olga_account)

Oleg.buy_artwork(girl_with_mandolin, 500,Oleg_account,margin)

#print(girl_with_mandolin)
print(Oleg_account)

print(market_place)
veneer.show_listings()





'''
Amazing! We built out a whole marketplace with buyers, sellers, art, and listings!

Here are some more things you could try:

Add a wallet instance variable to clients, update the buying and selling of artworks to also exchange dollar amounts.
Create a wishlist for your clients, things that are listed but they’re not sure if they should purchase just yet.
Create expiration dates for listings! Have out of date listings automatically removed from the marketplace.
'''

