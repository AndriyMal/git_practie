letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped = zip(letters,points)
#print(list(zipped))
letter_to_points ={key:value for key,value in zipped}

letter_to_points[' '] =0

def score_word(word):
  count = 0
  for i in word:
      try:
        count+=letter_to_points[i]
      except KeyError:
        word_up = i.upper()
        count+=letter_to_points[word_up]
  point_total = 0 
  for i in word:
      temp = letter_to_points.get(i,0)
      point_total +=temp
  return point_total

brownie_points = score_word('feWfwe')

print(brownie_points)


player_to_words = {'player1':['BLUE','TENNIS','EXIT'],'wordNerd':['EARTH','EYES','MACHINE'],'Lexi':['ERASER','BELLY','HUSKY'],'Prof Reader':['ZAP','COMA','PERIOD']}

player_to_points = {}

def update_point_totals(word):
  for player,words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points+= score_word(word)
    player_to_points[player] = player_points
  return player_to_points
print(update_point_totals('Lexi'))

def play_word(player,word):
  player_to_words[player].append(word) 

play_word('Lexi','CODE')



                 