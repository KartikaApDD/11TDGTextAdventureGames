#---functions---
class Game():
    def __init__(self):
        self.start_game()

#---MAIN CODE---

#welcome user + intro
    def start_game(self):
        name = input("What is your name?") 
        print("Welcome to the adventure game! This gonna be really funny,",name)
        print("Want to know what is your task that you need to solve on this game?. You JUST GET one question when you starting the game and of course you need to answer it! If you are incorrect, you can't escape and back to your world! Get correct answer and one apple to escape, but don't worry I will give you some story line that might be can help you to answer the question. We will you give some options to go, choose the best choices! Good luck, player.")
#introduction bg story game
        print("This is what the games about, i will explain before you will need to start the real game!")
        print("There is a girl who is hated with a lot of people with no reason, her family and her friends do not even talk with her. Whenever she goes to her family village their family is not even looking or talk with her. When she goes to the class to study their friends even does not talk with her and not looking at her like they can not see her. When she goes back to home her family do not even say hello to her and their face has no expression. Why their friends and family not talk with her even just say hello to her? Can you help to find the reason?")
        print("Hope you can escape, even though a bit chance to win this game ^^")
        self.main_room()
    def main_room(self):
        print("You need to choose your own path here! Please choose the best choices")
        choice = input("where you want to go? (village/class/house/exit):").upper()

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