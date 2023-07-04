import random

def playing_status():
    possible_responses = ["Y", "N"]
    while True:
        try:
            response = input("Would you like to play again ?")
            if response not in possible_responses:
                raise ValueError("Y and N only")
            if response == "Y":
                return True
            else:
                print("Thanks for Playing")
                exit()
        except ValueError as err:
            print(err)




print ("Welcome to Rock, Paper, Scissors")

def play_rps():
    play = True
    while play:
        print("Make your choice: [R][P][S]")
        player_choice = input()

        choices = ["R", "P", "S"]
        cpu_choice = random.choice(choices)

        print(cpu_choice)

        if cpu_choice == player_choice:
            print("Tie")
            play = playing_status()
        elif cpu_choice == "R" and player_choice == "P":
            print("You win")
            play = playing_status()
        elif cpu_choice == "R" and player_choice == "S":
            print("I win")
            play = playing_status()
        elif cpu_choice == "P" and player_choice == "R":
            print("I win")
            play = playing_status()
        elif cpu_choice == "P" and player_choice == "S":
            print("You win")
            play = playing_status()
        elif cpu_choice == "S" and player_choice == "R":
            print("You win")
            play = playing_status()
        elif cpu_choice == "S" and player_choice == "P":
            print("I win")
            play = playing_status()

if __name__ == '__main__':
   play_rps()
