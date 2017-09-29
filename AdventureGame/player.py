__author__ = 'Kenny'
import endgame

class Player:
    """Represents a player"""
    def __init__(self, name):
        self.name = name
        self.health = 100 # Player's starting health
        self.pos_x = self.pos_y = (5, 5) # Player's starting position
        self.victory = False # Determines if player has won the game

    def get_name(self):
        """Returns this player's name."""
        return self.name

    def take_damage(self, damage=0, multiplier=1):
        damage_taken = (damage * multiplier)
        print('You take %s damage!' % damage_taken)
        self.health -= damage_taken
        if not self.alive():
            print("\nYour health has run out!")
            endgame.lose_game()
        return self.health


    def alive(self):
        """If health drops to 0 player is dead, game over"""
        return self.health > 0


def make_player():
    """Asks the user for a name then returns a new Player with the specified info."""
    player_name = input("You awake in a very dark space, it is cold, damp... a cave?\n"
                        "You struggle to even remember your own name.\n"
                        "\nIt comes to you and you softly whisper it to yourself.\n"
                        "My name... it's: ")
    return Player(player_name)