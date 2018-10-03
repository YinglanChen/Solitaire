import numpy as np
from cards import Card, Pack, Stock, Tableau, Foundations
from game import Game
from os import system, name 
from time import sleep 

def print_instructions():
    print("Instructions: ")
    print("    'n'  to draw a card from stock")
    print("    'sf' to move a card from stock to foundations")
    print("    'tf' to move a card from tabulate to foundations")
    print("    'st col' to move a card from stock to the end of tabulate column[col]")
    print("    'tt c1 r1 c2' to move the pile start at col=c1, row = c2, to col=c2")
    print("Error messages are provided at the top of the game screen if the move is Illegal")

def main():    
    pack = Pack()
    game = Game(pack) 
    print("Welcome to Solitaire!") 
    print("Resize terminal or change font size for better experience")
    print("Enter 'start' to start the game! ")
    print("Instructions: ")
    print("    'i' to show this instruction message")
    print("    'n'  to draw a card from stock")
    print("    'sf' to move a card from stock to foundations")
    print("    'tf' to move a card from tabulate to foundations")
    print("    'st col' to move a card from stock to the end of tabulate column[col]")
    print("    'tt c1 r1 c2' to move the pile start at col=c1, row = c2, to col=c2")
    print("Error messages are provided at the top of the game screen if the move is Illegal")
    while True:
        s = input("hit Enter to start the game:")
        game.draw()
        break
    while True:

        print("Enter 'i' and scroll up (a little bit) for instructions")
        s = input("Enter your next move: ")
        if (s == "i"):
            print_instructions()
        elif (s == "n"):
            game.stock_next()
        elif (s == "sf"):
            game.stock_to_foundations()
        elif (s.startswith("st")):
            try:
                cmd = s.split(" ")
                c = cmd[1]
                game.stock_to_tabuleau(int(c))
            except:
                print("Illegal command. Missing argument(s).")
        elif (s.startswith("tf")):
            try:
                cmd = s.split(" ")
                c = cmd[1] 
                game.tabuleu_to_foundations(int(c))
            except:
                print("Illegal command. Missing argument(s).")
        elif (s.startswith("tt")):
            try:
                cmd = s.split(" ")
                c1 = cmd[1] 
                r1 = cmd[2]
                c2 = cmd[3]
                game.between_tabuleau(int(c1), int(r1), int(c2))
            except:
                print("Illegal command. Missing argument(s).")
        else:
            print("Unknow command")

        game.draw()
        if (game.win()):
            print("YOU WIN!!!!!!")
            break



if __name__ == '__main__':
    main()