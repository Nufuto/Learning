import random

bomb = random.randint(2, 99)
min_num = 1
max_num = 100

while True :
  try :
    guess = int(input("Your Turn...  "))

    if guess < min_num or guess > max_num:
      print("Out of range")
      continue
    elif guess > bomb:
      print("Too hight")
      max_num = guess
    elif guess < bomb:
      print("Too low")
      min_num = guess
    elif guess == bomb:
      print("Game Over")
      break
  except ValueError:
    print("Please Enter Number Only")
