print("Program Started!")

print("Please enter an ASCII code:\n")
code = int(input())

if code >= 32 and code <=126:
    print("The character represented by the ASCII value {} is {}:".format(code, chr(code)))
else:
    print("The character cannot be displayed.")

print("Program Ended!")
