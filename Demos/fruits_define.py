def get_fruits():
    fruits = []
    print("How many would you like to insert?")
    n = int(input())

    for i in range(n):
        print("Type in the next fruit:")
        fruits.append(input())
    print("Your fruits are {}".format(fruits))
    print(f"sliced list: {fruits[0:5:2]}")

get_fruits()


