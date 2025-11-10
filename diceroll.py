import random as r
def game():
  number = r.randint(0,10)
  attempts = 6
  guessed = False
  while attemps != 0 and not guessed:
    ask = int(input("what number would you like to guess?: "))
    if ask != number:
      print("failure")
      attempts -=1
    else:
      print("correct")
      attempts -=1
      guessed = True
  return False

a = True
while a:
  a= game()
