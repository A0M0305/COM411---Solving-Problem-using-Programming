print("What is your name?")
n = input()
print("Do you have a dog? (True or False)")
dog = bool(input())


if len(n) > 9 and dog == "True":
  print("You have a very long name!")
  print("Your name contains {} letters".format(len(n)))
else:
  print("Your name is quite okay")
  print("Your name contains {} letters.".format(len(n)))

print("This is the END of the program!")