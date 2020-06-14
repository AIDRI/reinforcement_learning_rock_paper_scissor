from collections import Counter
from random import choices, choice
from itertools import chain, cycle
from pprint import pprint
from utils_grl import select_proportional, select_maximum, random_reply
from utils_grl import single_event_proportional, single_event_greedy
from utils_grl import digraph_event_proportional, digraph_event_greedy

scorer = dict(SP=1, PR=1, RS=1, PS=-1, RP=-1, SR=-1, SS=0, PP=0, RR=0)
ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
options = ['R', 'P', 'S']
strategies = [random_reply, single_event_proportional, single_event_greedy,
              digraph_event_proportional, digraph_event_greedy]

def human_(opposition, strategies=strategies,
                   trials=100000, verbose=False):
    strategy_range = range(len(strategies))
    weights = [1] * len(strategies)
    p1hist = []
    p2hist = []
    cum_score = 0
    print(range(trials))
    for trial in range(trials):
        our_moves = [strategy(p1hist, p2hist) for strategy in strategies]
        i = choices(strategy_range, weights)[0]
        our_move = our_moves[i]

        opponent_move = opposition(p2hist, p1hist)

        score = scorer[our_move + opponent_move]
        if verbose:
            print(f'{our_move} ~ {opponent_move} = {score:+d}'
                  f'\t\t{strategies[i].__name__}')
            print(p1hist)
            print(p2hist)
        cum_score += score

        p1hist.append(our_move)
        p2hist.append(opponent_move)
        for i, our_move in enumerate(our_moves):
            if scorer[our_move + opponent_move] == 1:
                weights[i] += 1

    print(f'---- vs. {opposition.__name__} ----')            
    print('Total score:', cum_score)
    pprint(sorted([(weight, strategy.__name__) for weight, strategy in zip(weights, strategies)]))

if __name__ == '__main__':

    def human(p1hist, p2hist):
        return input(f'Choose one of {options!r}: ')

    human_(opposition=human, trials=100, verbose=True)