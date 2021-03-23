# Program that imitates a small database in the sense that it can:
# insert new student
# keep continually adding
# print out students name and mark
# average mark of all students
# find the maximum mark among all students

def generate_stds():
    print("Enter the name of the student: ")
    name = input()
    print("Enter the grade: ")
    grade = int(input())
    return name, grade


def all_stds():
    all_students = []
    while True:  # while loops are to continually add rather then for loop as this is when you know how many.
        all_students.append(generate_stds())
        print("Press Enter to continue, type 0 to finish")
        x = input()
        if x == '0':
            break  # This is to quit looping
    return all_students


def print_students(lista):
    for std in lista:
        print(f"{std[0]} earned a grade {std[1]}")


def avr_marks(lista):
    total = 0
    for std in lista:
        total += std[1]
    return total / len(lista)  # len tells you the size of the file stored.


print(avr_marks(all_stds()))
