import random

def guess_number():
    hidden_number = random.randint(1, 10)
    your_input = 0

    while your_input != hidden_number:
        your_input = int(input("Enter 1 - 10 number:- "))

        if your_input < hidden_number:
            print("Too low. Try again!")
        if your_input > hidden_number:
            print("Too high. Try again!")

    print("You won! Yeah")

guess_number()

