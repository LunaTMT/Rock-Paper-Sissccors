import os
import random
import time

class Player:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.score = 0
        self.choice = 0
    def __str__(self):
        return f"{self.name:>10} : {self.score:>10}"
    
    def get_choice(self):
        clear_con()
        print(f"""
        {self.name}'s move:
        1. Rock
        2. Paper
        3. Scissors
        """)
        
        choice = input(f"\tPlease Choose: ")
        choice = str(choice)
        while choice not in ("1", "2", "3"):
            choice = input(f"\tInvalid! Please choose again: ")

        self.choice = ("Rock", "Paper", "Scissors")[int(choice)-1]

class Ai(Player):
    def __init__(self):
        self.name = "Computer"
        self.score = 0
        self.choice = 0
    
    def get_choice(self):
        clear_con()
        self.choice = ("Rock", "Paper", "Scissors")[random.randint(0, 2)]

class Menu:

    def show_scores(p1, p2):
        clear_con()
        print("Score")
        print(p1, p2)
    def show_game_options():
        print("""
        ᏒᎧፈᏦ ᎮᏗᎮᏋᏒ ᏕፈᎥᏕᏕᎧᏒᏕ

        Which would you like to play?

        1: Player VS Player
        2: Player VS Computer
        Q: Quit
        """)    
    def show_score(players):
        clear_con()

        p1, p2 = players
        print(f"""
        \tScore
        | {p1} |   
        | {p2} |   
        """)

def get_game_option():
    choice = input("\tChoice : ")
    choice = str(choice)
    while choice not in ("1", "2", "Q"):
        choice = input("\tChoice : ")
    return choice
def get_players(game_choice):
    clear_con()

    print("\t\nPlayer 1,", end = " ")
    p1 = Player()

    print("\t\nPlayer 2,", end = " ")
    p2 = Player() if game_choice == 1 else Ai()
    
    return (p1, p2)
def get_winner(players):
    rules = {"Rock"     : "Scissors",            
             "Paper"    : "Rock",           
             "Scissors" : "Paper"}           

    p1, p2 = players
    identical = (p1.choice == p2.choice)
    p1_can_beat = rules[p1.choice] 

    if identical:
        return False

    winner, oponent = players if p1_can_beat == p2.choice else players[::-1]
    print(f"\t\n{winner.choice} beats {oponent.choice}")
    time.sleep(2)
    return winner

def clear_con():
    clear = lambda: os.system('clear')
    clear()


if __name__ == "__main__":
    clear_con()

    menu = Menu
    while True:
        
        menu.show_game_options()
        game_choice = get_game_option()
        if game_choice == "Q":
            break
        
        players = get_players(game_choice)

        for p in players:
            p.get_choice() 
        
        for p in players:
            print(f"{p.name :>10} chose {p.choice :>10}")
        time.sleep(2)

        winner = get_winner(players)
        if winner:
            print(f"\t\t\nWinner : {winner.name}")
            winner.score += 1
        else:
            print("\n             Draw!")
        time.sleep(2)
        
        menu.show_score(players)
        


