print("Towards which direction should I paint? Up, Down, Left or Right?")
print()

up = "Upwards"
down = "Downwards"
left = "Leftwards"
right = "Rightwards"

Dir = str(input("Which way?\n"))

if Dir == "up":
  print("I am painting {} direction.".format(up))
elif Dir == "down":
  print("I am painting {} direction.".format(down))
elif Dir == "left":
  print("I am painting {} direction.".format(left))
elif Dir == "right":
  print("I am painting {} direction.".format(right))
else:
  print("Paint it yourself then")
