import random

coin=["Head","Tail"]

while True:
  ai_choice=random.choice(coin)
  print(ai_choice)

  print("\n 1) Continue 2) Quit\n")
  selection=int(input("Enter Choice : "))
  if selection==2:
    break
