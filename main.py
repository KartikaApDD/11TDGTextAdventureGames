class Game:
    def __init__(self):
        self.inventory = []
        self.start_game()

#---functions---

# Welcome user and introduce the game
def intro(): 
    # ask name of user       
    name = input("What is your name?")
    #welcom user
    print("Welcome to the adventure game!,",name)
    print("Want to know what is your task that you need to solve on this game?")
    #intro of game
    print("You will get some of question when you starting the game and of course you need to answer it! If you are incorrect, you die!")
    print("You need to get at least 1 apple to end the game and escape, but how to get that apple?")
    print("I will provide story that can support you to answer the question on the game and there might be a hint on the question and hopiing you can solve it, dear player ^^")
    print("This is the time, goodluck")

#introduction bg story game
def start_game(self):
    print("This is what the games about, i will explain before you will need to start the real game!")
    print("put story")
    print("Hope you can escape, even though a bit chance to win this game ^^")
    self.main_room()
def main_room(self):
    print("You need to choose your own path here! Please choose the best choices")
    choice = input("where you want to go? (village/class/house/exit):").capitalize()

    if choice == "village":
        self.village_room()
    elif choice == "class":
        self.class_room()
    elif choice == "house": 
        self.house_room()
    elif choice == "exit":
        print("You can't go before start the game, sorry!")
        self.main_room()
    else:
        print("greattt!")
