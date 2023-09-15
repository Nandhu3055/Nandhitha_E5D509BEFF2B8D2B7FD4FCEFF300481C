class Player:
  def play(self):
    print("The Player is palying cricket")
class Batsman(Player):
  def play(self):
    print("The Batsman is batting") 
class Bowler(Player):
  def play(self):
    print("The Bowler is Bowling")    

x = Batsman()
x.play()
x = Bowler()
x.play()


