#!/usr/bin/env python

# Welcome the user and provide a menu
while True:
  print("Welcome to Python Savings.")
  print("Choose from one of the tasks below.")
  print("1. Add Savings.")
  print("2. View Savings.")
  print("3. Quit Program.")

  choice = input("From the items above make a select from 1 - 3: ")

  if (int(choice) == 3):
    break
  elif (int(choice) < 3):
    if (int(choice) == 1):
      print("\nYou picked {}\n".format(choice))
    else:
      total = 0
      f = open("savings.txt", "r")
      savings_from_file = f.readlines()
      f.close()

      for i in savings_from_file:
        total += int(i)
      print("\nI have saved ${} so far this year\n".format(total))
  else:
    print("\nYou have made an invalid choice, please try again\n")
