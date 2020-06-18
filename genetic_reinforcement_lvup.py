from collections import Counter
from random import choices, choice
from itertools import chain, cycle
from pprint import pprint
from utils_grl import sp, sm, rr
from utils_grl import sep, seg
from utils_grl import dep, deg
import time
#Import all librairies and functiion who I need

scorer = dict(SP=1, PR=1, RS=1, PS=-1, RP=-1, SR=-1, SS=0, PP=0, RR=0) #This is the scorer, with it, I can have the score for every battle
rps = ['R', 'P', 'S'] #This is all move who the bot can understand and play
strategies = [rr, sep, seg, dep, deg] #Here, all strategies, to understand each strategies, go to utils

def human_(opposition, rounds = 20, strategies=strategies): #functiun to play : opposition = human, we called the function to ask the move to the player, strategies is my list of strategies
    strategy_range = range(len(strategies)) # equal to (0, 5) because I have 5 strategies : 0, 1, 2, 3, 4.
    weights = [1] * len(strategies) #the weights for the strategies
    bot = []
    player = []
    pre = 0
    num_it = 0
    cum_score = 0 #initialize history move (bot and player) and the end score
    print(range(rounds)) #print the range of my rounds : (0, 20)
    for trial in range(rounds): #repeat the loop 20 times
        bot_m_all = [strategy(bot, player) for strategy in strategies] #here, we are playing all possibe move with all strategies
        i = choices(strategy_range, weights)[0] #here, we are define the strategie in i
        bot_m = bot_m_all[i] #and finally, we are define the bot's move in bot_m
        #asking the move of the player : oppostion() called the function human()
        while num_it == pre:
            player_m, num_it = opposition(player, bot)
            print(player_m, num_it)
            time.sleep(0.05)

        pre = num_it
        print(bot_m,player_m)
        score = scorer[bot_m + player_m] #now we can score the round : exemple : R (bot) vs P (player) = -1 for the bot
        print(f'{bot_m} ~ {player_m} = {score:+d}' #print the log of the match
              f'\t\t{strategies[i].__name__}') #print the strategie used by the bot
        cum_score += score #add score (in my exemple minus 1) to the total score

        bot.append(bot_m) #add bot move to history
        player.append(player_m) #add player move to history
        for i, bot_m in enumerate(bot_m_all): #for all my strategies
            if scorer[bot_m + player_m] == 1: #if we win
                weights[i] += 1 #we modify weights to give more importance of this particular weight
        with open("response.txt", "w+") as q:
            q.write(bot_m)

    print('Total score:', cum_score) #add the end of the game (20 rounds) we print the total score (0 means 10 vitories and 10 looses, +5 means 15 victories and 5 looses, and more)



def human(bot, player): #it is the function to ask the player to move.
    with open("markov.txt", "r") as s: #we return him choice between R (rock) P (paper) S (scissors)
        for line in s:
            return line[0], line[1]



pre_match = 0

while True:
    with open("markov.txt", "r") as f:
        for line in f:
            if pre_match != int(line[2]):
                pre_match = int(line[2])
                human_(opposition=human, rounds=20) #called the function human_ : oppositon is the game mode (only one currently), and round is the number of rounds, I think 10 or 15 is the min to have good performances
