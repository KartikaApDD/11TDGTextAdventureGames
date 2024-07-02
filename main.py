#---functions---
class Game():
    def __init__(self):
        self.start_game()

#---MAIN CODE---

#welcome user + intro
    def start_game(self):
        print("Hello! Welcome to the adventure game, dear player!")
        #story line
        choice = input("Do you wish to read the story or just want skip it? I suggested to read the story for better experience!(skip/continue)):")
        #choice for storyline
        if choice == "skip":
            self.start_game()
        elif choice == "continue":
            self.main_room()

#story line, starting game
    def main_room(self):
        print("Here is the story: There is a girl named Diana, she just turned 15 years old this month. She looks lonely because her friends and family suddenly ignore her and look like they hate her so much. She does not have any idea why they become cold towards her, unbelievable. When she goes to her class her friend just pass her without say anything, same with her family. She hates to be lonely.")
        print("You need to choose your own path here! Please choose the best choices")
        choice = input("where you want to go? (village/class/house/exit):")

        if choice == "village":
            self.village_room()
        elif choice == "class":
            self.class_room()
        elif choice == "house":
            self.house_room()
        elif choice == "exit":
            print("You can't go before start the game, sorry!")
        else:
            print("Great!")
            self.main_room()

#---ROOM---
#village
    def village_room(self):
        print("Welcome, you have entered the village")
        choice = input("You just passed your family without communicate. Your holiday has ended and you need to go back. Do you want to go back with your family? (yes/no/no idea):").lower()

        if choice == "yes":
            self.house_room()
        elif choice == "no":
            self.class_room()
        elif choice == "no idea":
            print("No idea? Take your time to choose")
        else:
            print("Please choose")
            self.village_room()
#house
    def house_room(self):
        print("Good! You can't escape, good bye")
#class
    def class_room(self):
        print("Great choice! You see there a flower on that girl tables? That is Chrysanthemums, do you know what that means?")
        player = input("")

        if player == "I don't know":
            self.class_room()
            print("Try to answer, please!!!!")
        elif player == "Is she died a long ago???":
            print("You are correct, you get 1 apple. She died a long time ago but she still does not believe that she has died. They ignore her because they can not she her. Her family regret that they treat her really bad when she still alive. That poor girl still not believe but because you are in her body and you solve it that girl can live in peace now. Thanks for you")
            self.main_room()
#---RUN---
Game()