n = int(input("Please enter a whole number:\n"))

num = n%2

if num == 0:
  print("The number {} is an even number".format(n))
elif num == 1:
  print("The number {} is an odd number".format(n))