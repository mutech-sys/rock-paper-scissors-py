import random

user_points = 0
computer_points = 0

# r: rock , p:paper, s:scissors
options = ['r', 'p', 's']

print(r"WELCOME TO ROCK/PAPER/SCISSORS")

while True:
    print()
    user_choice = input(r"Enter your choice(r,s,p) or `q` to quit: ").lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        print("ENTER A VALID OPTION!!")
        print()
        continue

    # random number for computer's choice. 
    # 0:r, 1:s, 2:p
    random_number = random.randint(0,2)

    # computer choosing a random choice 
    computer_choice = options[random_number]

    if user_choice == 'r' and computer_choice == 's':
        print("COMPUTER CHOICE:", computer_choice)
        print('USER WON!!')
        user_points += 1
        continue
    elif user_choice == 's' and computer_choice == 'p':
        print("COMPUTER CHOICE:", computer_choice)
        print('USER WON!!')
        user_points += 1
        continue
    elif user_choice == 'p' and computer_choice == 'r':
        print("COMPUTER CHOICE:", computer_choice)
        print('USER WON!!')
        user_points += 1
        continue
    elif user_choice == computer_choice:
        print("COMPUTER CHOICE:", computer_choice)
        print("TIE!!")
        continue
    else:
        print("COMPUTER CHOICE:", computer_choice)
        print("COMPUTER WON!!")
        computer_points += 1
        continue

print()
print("SCOREBOARD:")
print("USER POINTS: ", user_points)
print("COMPUTER POINTS: ", computer_points)
print()

print("GoodBye!!!")