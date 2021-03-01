# Inputting human data

print("What is your name?")
Name = input()
print("How old are you?")
Age = int(input())
print("How tall are you? in cm")
Height = float(input())
print("What is your weight?")
Weight = float(input())
BMI = Weight/((Height/100)*(Height/100))

print(Name, "you are", Age, "years old and your BMI is", round(BMI,2),".")
