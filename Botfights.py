#!/usr/bin/env python
# coding: utf-8

from Bots2 import *
import random



def match(player1, player2):
    # the number of which turn we are on
    turn = 0

    # The health number of each player.
    # When it is zero, the player dies
    player1_life = 100
    player2_life = 100





    while player1_life > 0 and player2_life > 0:
        turn = turn + 1

        # get the accuracy power and defense dict from Bots class
        p1 = player1.turn(player1_life, player2_life)
        p2 = player2.turn(player2_life, player1_life)

         # disqualifing cheating
        if p1['accuracy']+p1['power']+p1['defense'] != 10 or p1['accuracy'] < 0 or p1['defense'] < 0 or p1['power'] < 0:
             player1_life = 0
             print(f"{player1.name} is disqualified for illegal turn powers: {p1['accuracy']}, {p1['power']}, {p1['defense']}")

        if p2['accuracy']+p2['power']+p2['defense'] != 10 or p2['accuracy'] < 0 or p2['defense'] < 0 or p2['power'] < 0:
             player2_life = 0
             print(f"{player2.name} is disqualified for illegal turn powers: {p2['accuracy']}, {p2['power']}, {p2['defense']}")

        # check if they are dead
        if player1_life == 0 or player2_life == 0:
            break


        # maching up the bots power to the botfights damage
        player1_damage = p1['power']

        # ?
        if random.uniform(0,10) <= p2['accuracy']:
            player1_damage = p1['power'] - p2['defense']


        # canceling cheating
        if player1_damage < 0:
            player1_damage = 0

        # player1 hits player2
        if random.uniform(0,10) <= p1['accuracy']:
            player2_life = player2_life - player1_damage
        # seting a varubule
        player2_damage = p2['power']

        # ?
        if random.uniform(0,10) <= p1['accuracy']:
            player2_damage = p2['power'] - p1['defense']

        # more canceling cheating
        if player2_damage < 0:
            player2_damage = 0

        # player2 whacking player1
        if random.uniform(0,10) <= p2['accuracy']:
            player1_life = player1_life - player2_damage


        print(f'Turn {turn}: {player1.name}, {player1_life}, {player2.name},  {player2_life}')

     # murdur
    if player1_life <= 0:
         print(f"{player1.name} loses!")
     # saving
    else:
         print(f"{player1.name} wins!")
     # dooming
    if player2_life <= 0:
         print(f"{player2.name} loses!")
     # taking out of the arina
    else:
         print(f"{player1.name} wins!")

match(Smart(), Rand())




