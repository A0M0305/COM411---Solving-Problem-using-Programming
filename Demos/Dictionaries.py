phonebook = {}

while True:
    name = input("Enter the name")
    number = input("Enter the number")
    phonebook[name] = number
    if input("Type 'x' to stop") == 'x':
        break


def calling(n, book=None):
    if book is None:
        book = {}
    print(f"Calling {n} with a phone number{book[n]}")


phonebook["Tadek"] = "8234528482"
