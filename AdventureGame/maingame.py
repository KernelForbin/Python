__author__ = 'KernelForbin'
import random
import time
import player
import endgame

"""Map of cave"""

player1 = player.make_player()

def play_game(player):
    print("\nA booming voice shakes the cave!\n"
          "WELCOME %s, can you find your way out? HA HA HA!" % player.get_name())

time.sleep(1)

play_game(player1)

print("\nYou are dumbfounded. Is this a dream? Never mind it. You must push on and get out of this cave!")

time.sleep(1)

print("You eyes are adjusted to the dark and you see shapes forming in front of you.")
print("You realize that you are in the middle of a room with two ways to go\n")

time.sleep(1)

print("You can go N (North), E (East)")

room_00 = input("Which direction will you go? ")

if room_00 == 'N':  # Leads to room_01
    print("\nYou slowly creep your way straight ahead, slipping through a narrow pathway in front of you\n"
          "In the next area you see two more pathways to the N or W\n"
          "You also see a large puddle of liquid on the ground, you're PRETTY sure it's water...")

    water_01 = input("\nDrink some of the liquid? Y or N: ")

    if water_01 == "Y":
        print("You approach the water, lean in, it seems okay... you take a small sip")
        water_01_effect = random.randint(0,1)
        if water_01_effect == 0:
            print("\nAck! Disgusting! Foul! Why did you do that?!")

            player1.take_damage(10)
            print('You have %s health remaining' % player1.health)

        if water_01_effect == 1:
             print("\nNot so bad, you feel refreshed!")
    if water_01 == "N":
        print("\nProbably a good call... best to move on")

    water_room = input("\nSo which way do you go? N or W? ")
    if water_room == "N":
        print("\nYou may your move further North and a deep rumble occurs.\n"
              "Rocks fall from the top of the cave and crush you in to oblivion")

        endgame.lose_game()

    if water_room == "W":
        print("\nYou head to the West and in to the next room. A swift breeze begins to blow\n"
              "The gust gets stronger, this doesn't seem right. You begin to hear a faint sound...")

        time.sleep(1)

        print("\nBATS!!!!\n"
              "A swarm of bats swirl around you in a flurry, make a choice!")

        bats_01 = input("\n1. Flail wildly?\n"
                        "2. Duck?\n"
                        "> ")
        if bats_01 == "1":
            print("\nYou flail like a madman and the bats are not pleased!\n"
                  "They nip away at you, it hurts... oh does it hurt, but they eventually tire of you and leave")

            player1.take_damage(20)
            print('You have %s health remaining' % player1.health)

        if bats_01 == "2":
            print("\nYou wisely duck for cover, the bats lose interest in the room, they eventually disperse, whew.")

    print("\nA rope hangs from places unknown, it looks quite sturdy. You also see small opening in the distance\n"
          "You may have to crawl through it...")

    bat_room = input("\n1. Climb the rope\n"
                     "2. Go towards the opening\n"
                     "> ")

    if bat_room == "1":
        print("\nYou begin to climb, you climb higher and higher, you see an opening to the side\n"
              "You could probably swing yourself over to it...\n")

    if bat_room == "2":
        print("\nYou squeeze yourself through the small opening at the far side of the room.\n"
              "You see a faint light up ahead, thing looks good!\n"
              "The space is getting more narrow, good thing you're not claustrophobic!\n"
              "But uhhhh, you're stuck. Annnnnnd you eventually die.")

        endgame.lose_game()

    rope_climb = input("\n1. Swing to the ledge\n"
                       "2. Keep climbing\n"
                       "> ")

    if rope_climb == "1":
        print("\nYou swing back and forth, getting closer and closer to the ledge\n"
              "You release at just the right time and reach the ledge just as you planned. Smooth.")

        print("\nIn this room there are 4 pedestals with buttons on them...")

        pedestal_choice = 0

        while pedestal_choice != "3":
            pedestal_choice = input("Which button will you press? 1, 2, 3, or 4? ")

            if pedestal_choice == "1":
                print("BEES!\n"
                      "BEADS? No. BEES! They swarm around you, stinging until they all die off.")
                player1.take_damage(30)
                print('You have %s health remaining' % player1.health)

            if pedestal_choice == "2":
                print("DOGS!\n"
                      "Wild dogs rush you from all sides and bite you repeatedly, ow ow ow\n"
                      "They, for apparently no reason at all, rush off of the side of the cliff you came from\n"
                      "But they left you hurting badly")
                player1.take_damage(50)
                print('You have %s health remaining' % player1.health)


            if pedestal_choice == "4":
                print("Dogs with bees in their mouths! When they bark, they shoot bees at you!\n"
                      "This is pretty much a worst-case-scenario situation.")
                player1.take_damage(90)
                print('You have %s health remaining' % player1.health)

        time.sleep(2)

        print("Wise choice! The wall in front of you parts and you are met with a great bright white light!")

        endgame.win_game()

    if rope_climb == "2":
        print("You keep on climbing, gym class is really paying off here.\n"
              "You climb, and climb, and climb, and climb... this is getting exhausting.\n"
              "\nIt looks like you may be nearing the top! Yes! You found where the rope attaches! Hurray!")

        time.sleep(1)

        print("\nHmmm, maybe this wasn't a great idea, there's nothing here, just rock\n"
              "You've been on this rope a bit too long, it begins to fray, oh boy.")

        time.sleep(1)

        print("\nYou begin to rapidly climb down... but it's just too late. The rope snaps and you fall.")

        time.sleep(1)

        endgame.lose_game()


if room_00 == "E":
    print("You head East with determination. You WILL get out of this cave!\n")

    time.sleep(2)

    print("Your ego is immediately deflated when you come across a room full of skeletons\n"
          "You die. Not very interesting, I know...\n")

    endgame.lose_game()
