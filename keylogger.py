import random

random_number = round(random.random()*20)

print(str(random_number)[0])

input_number = int(input("Enter a number between 0 with 20:"))

while random_number != input_number:
    if input_number > random_number:
        print("You entered a large number!")
    else:
        print("You entered a small number")

    input_number = int(input("Enter a number between 0 with 20:"))

print("YOU ARE WON!!")





