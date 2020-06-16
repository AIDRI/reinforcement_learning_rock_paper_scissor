from collections import Counter
from random import choices, choice
from itertools import chain

rps = ['R', 'P', 'S'] #all possible moves
rep = {'P': 'S', 'R': 'P', 'S': 'R'} #reponse for each case

#Here, I am just going to define all functions and strategies

def sp(events, baseline=()): #just a utility function to select proportionally a move
    rel_freq = Counter(chain(baseline, events))
    p, weights = zip(*rel_freq.items())
    return choices(p, weights)[0]

def sm(events, baseline=()): #just a utility function  to select the max / or most common move
    rel_freq = Counter(chain(baseline, events))
    return rel_freq.most_common(1)[0][0]

def rr(bot, player):    #random answer
    return choice(rps) #we are just return a random choice in the rps list with the function choice import from random

def sep(bot, player):   #it is a proportionnal function : when opponent play 1/3 time S, we are playing R 1/3 time randomly
    pred = sp(player, rps)  #we are calling the sp utility function (see above)
    return rep[pred] #finally, we return the inverse of the moov selecting

def seg(bot, player):   #when player plays P more than R and S, we always play S
    pred = sm(player, rps) #we are calling the sm utility function (see above)
    return rep[pred] #finally, we return the inverse of the move selecting

def dep(bot, player): #When opponent's most recent play is S and they usually play R two-thirds of the time after an S, respond with P two-third of the time.
    rp = player[-1:] #get the previous move
    d = zip(player, player[1:]) #create a diagraph of previous move to see what the layer usually do
    f = [b for a, b in d if a == rp] #detect the "followers" previous moves
    pred = sp(f, rps) #select proportionnaly with sp (see above)
    return rep[pred] #return the inverse of the move selecting

def deg(bot, player):#When opponent's most recent play is S and they usually play R two-thirds of the time after an S, respond with P two-third of the time.
    rp = player[-1:] #gt the previous move
    d = zip(player, player[1:])#create a diagraph of previous move to see what the layer usually do
    f = [b for a, b in d if a == rp] #detect the "followers" previous moves
    pred = sm(f, rps) #select most common with sm (see above)
    return rep[pred] #return the inverse pf the move selecting
