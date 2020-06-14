from collections import Counter
from random import choices, choice
from itertools import chain
options = ['R', 'P', 'S']
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
def select_proportional(events, baseline=()):
    rel_freq = Counter(chain(baseline, events))
    population, weights = zip(*rel_freq.items())
    return choices(population, weights)[0]

def select_maximum(events, baseline=()):
    rel_freq = Counter(chain(baseline, events))
    return rel_freq.most_common(1)[0][0]

def random_reply(p1hist, p2hist):
    return choice(options)

def single_event_proportional(p1hist, p2hist):
    prediction = select_proportional(p2hist, options)
    return ideal_response[prediction]

def single_event_greedy(p1hist, p2hist):
    prediction = select_maximum(p2hist, options)
    return ideal_response[prediction]

def digraph_event_proportional(p1hist, p2hist):
    recent_play = p2hist[-1:]
    digraphs = zip(p2hist, p2hist[1:])
    followers = [b for a, b in digraphs if a == recent_play]
    prediction = select_proportional(followers, options)
    return ideal_response[prediction]

def digraph_event_greedy(p1hist, p2hist):
    recent_play = p2hist[-1:]
    digraphs = zip(p2hist, p2hist[1:])
    followers = [b for a, b in digraphs if a == recent_play]
    prediction = select_maximum(followers, options)
    return ideal_response[prediction]