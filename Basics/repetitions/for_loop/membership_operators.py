print("What phrase do you see?")
phrase = input()

print("\nReversing...\nThe phrase is\n", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)
