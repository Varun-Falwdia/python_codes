import random
user_score = 0
computer_score = 0
item = ["Stone","Paper","Sciscor"]
print("Welcome in the Game :)")
player = input("Enter Your Name : ")
n = int(input("How many times do you want to play : "))
for i in range(1,n+1):
    computer = random.choice(item)
    print(f"computer = {computer_score}, {player} = {user_score}")
    print("Press 1 : Stone")
    print("Press 2 : Paper")
    print("Press 3 : Sciscor")
    user = int(input("Enter : "))
    if user == 1 and computer == "Paper":
        computer_score += 1
    elif user == 1 and computer == "Sciscor":
        user_score += 1
    elif user == 2 and computer == "Sciscor":
        computer_score += 1
    elif user == 2 and computer == "Stone":
        user_score += 1
    elif user == 3 and computer == "Stone":
        computer_score += 1
    elif user == 3 and computer == "Paper":
        user_score += 1
    print(f"\ncomputer choose {computer}")
print(f"computer = {computer_score}, {player} = {user_score}")
if user_score < computer_score:
    print("computer wins")
    print("Thank you for playing :)")
elif user_score > computer_score:
    print("You wins")
    print("Thank you for playing :)")
else:
    print("Match Tie Nobody Wins :(")
