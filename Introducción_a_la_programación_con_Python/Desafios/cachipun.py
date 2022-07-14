# The above code is a game of rock, paper, scissors.
import random

# Creating a list of options, and setting the user and computer counters to 0.
options = (["piedra", "papel", "tijera"])
user_counter = 0
computer_counter = 0

# This is the main loop of the game. It will keep running until the user decides to stop playing.
while True:
    while user_counter == 0 and computer_counter == 0:
        user = input("\nPiedra, Papel, Tijera? >> ").lower()
        computer = random.choice(["piedra", "papel", "tijera"])

        if user not in options:
            print("Ingrese solo piedra, papel o tijera")
            continue
        elif user == "piedra":
            user_counter = 1
        elif user == "papel":
            user_counter = 2
        else:
            user_counter = 3

        if computer == "piedra":
            computer_counter = 1
        elif computer == "papel":
            computer_counter = 2
        else:
            computer_counter = 3


    # This is the logic of the game.
    selecion = f"\nEl usuario seleccionó {user_counter} y el computador seleccionó {computer_counter}"
    if user_counter == computer_counter:
        print(selecion)
        print("Empate")
    elif user_counter > computer_counter:
        print(selecion)
        print("Gana el usuario")
    else:
        print(selecion)
        print("Gana el computador")

# This is the code that asks the user if they want to play again. If they do, the game will restart.
# If they don't, the game will end.
    play_again = input("\n¿Desea jugar otra vez? (s/n) >> ").lower()

    if play_again == "n":
        break
    else:
        user_counter = 0
        computer_counter = 0