import random
user_choice=int(input("enter your choie:"))
if user_choice >= 3 and user_choice <0:
    print("invalid choice you lose")
else:
    computer_choice=random.randint(0,2)
    print("Computer Chose:")
    print(computer_choice)
    if computer_choice == user_choice:
        print("its a draw")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif computer_choice == 2 and user_choice == 0:
        print("you win")
    elif computer_choice > user_choice:
        print("you loose")
    elif user_choice > computer_choice:
        print("you win")