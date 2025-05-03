import random

def welcome():
    print("Welcome to my funny game")
    print("Go go go")

def finish(number, count):
    print("Good game")
    print(f"my number was {number} and you found it in {count} quesses")
    answer = input("Do you want to play again? (N/Y)")
    if answer.upper() in ["Y", "YES"]:
        return True
    else:
        return False
        

def win(computer_number, quess):
    return computer_number == quess

def answer(computer, user):
    if computer > user:
        return "My number is larger"
    if computer < user:
        return "Mine is smaller"
    return "you won!"

def get_a_guess():
    ans = input("What's your quess?")
    return int(ans)

welcome()
continue_playing = True
while(continue_playing):

    computer_number = random.randint(1, 10)
    quess = 0
    count = 0

    while ( not win (computer_number, quess)):
        quess = get_a_guess()
        count += 1
        print(answer(computer_number, quess))

    continue_playing = finish(computer_number, count)