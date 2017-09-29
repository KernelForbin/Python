__author__ = 'computerlab'
import random
import os

def lose_game():
    lose_message = random.randint(0, 2)
    if lose_message == 0:
        print("The voice booms again: You lose! Although I'm somewhat disappointed, I thought you had it in you...")
    if lose_message == 1:
        print("The voice booms again: You lose! Just as I expected.")
    if lose_message == 2:
        print("The voice booms again: You lose! Time to find another poor soul for my cave.")

    quit()

def win_game():
    win_message = random.randint(0, 2)
    if win_game == 0:
        print("The voice booms: You... won?! Gah! NO! How can this be?!")
    if win_message == 1:
        print("The voice booms: You win! I can finally quit this terrible life and see my kids, woo!")
    if win_message == 2:
        print("The voice booms: You win! Back to your boring life... cool, enjoy that.")

    quit()