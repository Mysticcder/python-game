def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You can go left or right.")
    choice1 = input("Do you want to go left or right? (left/right): ").lower()

    if choice1 == "left":
        print("\nYou encounter a wild animal!")
        print("You can try to fight it or run away.")
        choice2 = input("Do you want to fight or run? (fight/run): ").lower()

        if choice2 == "fight":
            print("\nYou bravely fight the animal and win! You find a treasure chest.")
            print("You open the chest and find gold and jewels. You win!")
        elif choice2 == "run":
            print("\nYou run away safely, but you find yourself lost in the forest.")
            print("After wandering for hours, you find your way back home. The adventure ends here.")
        else:
            print("\nInvalid choice. The adventure ends abruptly.")

    elif choice1 == "right":
        print("\nYou find a peaceful clearing with a beautiful lake.")
        print("You can choose to relax by the lake or continue exploring the forest.")
        choice2 = input("Do you want to relax or explore? (relax/explore): ").lower()

        if choice2 == "relax":
            print(
                "\nYou relax by the lake and enjoy the serene surroundings. It's a peaceful ending to your adventure.")
        elif choice2 == "explore":
            print("\nYou explore the forest further and find a hidden cave.")
            print("Inside the cave, you discover ancient ruins filled with mysteries. Your adventure continues!")
        else:
            print("\nInvalid choice. The adventure ends abruptly.")

    else:
        print("\nInvalid choice. The adventure ends abruptly.")


if __name__ == "__main__":
    start_adventure()
