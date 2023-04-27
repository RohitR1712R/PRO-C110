import random

response = "y"

while response == "y":
    no = random.randint(1, 6)

    if no == 1:
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬜⬛⬜⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("Would you like to throw the 🎲 again? (y / n)")
        choice = input()
        if choice == "n":
            print("Thanks for playing with us! See you next time!")
            break
        else:
            print("")
    elif no == 2:
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬛⬜⬜⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬜⬜⬛⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("Would you like to throw the 🎲 again? (y / n)")
        choice = input()
        if choice == "n":
            print("Thanks for playing with us! See you next time!")
            break
        else:
            print("")
    elif no == 3:
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬛⬜⬜⬜]")
        print("[⬜⬜⬛⬜⬜]")
        print("[⬜⬜⬜⬛⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("Would you like to throw the 🎲 again? (y / n)")
        choice = input()
        if choice == "n":
            print("Thanks for playing with us! See you next time!")
            break
        else:
            print("")
    elif no == 4:
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬛⬜⬛⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬛⬜⬛⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("Would you like to throw the 🎲 again? (y / n)")
        choice = input()
        if choice == "n":
            print("Thanks for playing with us! See you next time!")
            break
        else:
            print("")
    elif no == 5:
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬛⬜⬛⬜]")
        print("[⬜⬜⬛⬜⬜]")
        print("[⬜⬛⬜⬛⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("Would you like to throw the 🎲 again? (y / n)")
        choice = input()
        if choice == "n":
            print("Thanks for playing with us! See you next time!")
            break
        else:
            print("")

    elif no == 6:
        print("[⬜⬜⬜⬜⬜]")
        print("[⬜⬛⬜⬛⬜]")
        print("[⬜⬛⬜⬛⬜]")
        print("[⬜⬛⬜⬛⬜]")
        print("[⬜⬜⬜⬜⬜]")
        print("Would you like to throw the 🎲 again? (y / n)")
        choice = input()
        if choice == "n":
            print("Thanks for playing with us! See you next time!")
            break
        else:
            print("")
