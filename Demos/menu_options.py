print("Please choose an option from the menu:\n1 - Nice message\n2 - Area of a rectangle\n3 - Area of a Triangle\n4 - Times Table")
print()

option = int(input("What is your choice\n"))
print()

if option == 1:
  print("Today will be a very nice day.")

elif option == 2:
  print("What is the length?")
  l = int(input())
  print("What is the Width?")
  w = int(input())
  area = l*w
  print("The area of your rectangle is {}:".format(area))

elif option == 3:
  print("What is the base?")
  b = float(input())
  print("What is the height?")
  h = float(input())
  area = 0.5*b*h
  print("The area of your triangle is {:.2}:".format(area))

elif option == 4:
  print("Which times table would you like to see?")
  n = int(input())
  for i in range(1,11,1):
    print("{}x{} = {}".format(n, i, n*i))

else:
  print("There is no such option, go to Spec Savers")
