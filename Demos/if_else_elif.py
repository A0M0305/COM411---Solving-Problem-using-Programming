print("What is your name?")
n = input()
# print("Do you have a dog? (True or False)")
# dog = input()

if len(n) > 9:
    print("You have a very long name!")
elif len(n) > 6:
    print("Your name is a bit long. Consider a nickname")
elif len(n) < 3:
    print("Your name is very short.")
else:
    print("Your name is quite okay")

print("Your name contains {} letters.".format(len(n)))
print("This is the END of the program!")
