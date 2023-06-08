import random
while True:
    choices =['rock','paper','scissor']
    computer=random.choice(choices)
    human=None

    while human not in choices:
        human=input("rock,paper or scissor??:").lower()
        print("choose between 3 options please !")

    if human==computer:
        print("human:",human)
        print("computer:",computer)



        print("tie !")
    elif human=="rock":
        if computer=="paper":
            print("human:", human)
            print("computer:", computer)
            print("computer wins !")
        if computer=="scissor":
            print("human:", human)
            print("computer:", computer)
            print("you win !")
    elif human=="scissor":
        if computer=="paper":
            print("human:", human)
            print("computer:", computer)
            print("you win !")
        if computer=="rock":
            print("human:", human)
            print("computer:", computer)
            print("computer wins !")
    elif human=="paper":
        if computer=="scissor":
            print("human:", human)
            print("computer:", computer)
            print("computer wins !")
        if computer=="rock":
            print("human:", human)
            print("computer:", computer)
            print("you win !")

    play_again=input("play again yes or no?").lower().strip()
    if play_again != "yes":
            break
print("Bye!")