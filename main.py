class game:
    def in_it(self):
        self.start_game()
        self.intro()
#---functions---

# Welcome user and introduce the game
    def intro(self): 
        # ask name of user       
        name = input("What is your name?")
        #welcom user + intro
        print("Welcome to the adventure game!,",name)
        print("Want to know what is your task that you need to solve on this game?. You JUST GET one question when you starting the game and of course you need to answer it! If you are incorrect, you can't escape and back to your world! Get correct answer and one apple to escape, but don't worry I will give you some story line that might be can help you to answer the question. We will you give some options to go, choose the best choices! Good luck, player.")

#introduction bg   story game
    def start_game(self):
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
            self.main_room()
        else:
            print("greattt!")
