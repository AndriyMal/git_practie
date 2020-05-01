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

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    
    if self.is_museum == True:
      self.location = location
    else:
      self.location = "Private Collection"

  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      listing1 = Listing(artwork,price,self)
      veneer.add_listing(listing1)
  
  def buy_artwork(self, artwork):
      if artwork.owner != self:
        art_listing = 0
        for lst in veneer.listings:
         if lst.art == artwork:
             art_listing = lst
             lst.art.owner = self
             veneer.remove_listing(art_listing)
             break


moma = Client("The MOMA", "New York", True)

edytta = Client('Edytta Halpirt',None, False)

girl_with_mandolin = Art("Picasso, Pablo","Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '%s, %s. ' % (self.art.title,self.price)
    "{a} for {p}".format (a = self.art, p = self.price) 

edytta.sell_artwork(girl_with_mandolin,'$6M (USD)')

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)


veneer.show_listings()