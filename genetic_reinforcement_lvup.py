from collections import Counter
from random import choices, choice
from itertools import chain, cycle
from pprint import pprint
from utils_grl import sp, sm, rr
from utils_grl import sep, seg
from utils_grl import dep, deg

scorer = dict(SP=1, PR=1, RS=1, PS=-1, RP=-1, SR=-1, SS=0, PP=0, RR=0)
rps = ['R', 'P', 'S']
strategies = [rr, sep, seg, dep, deg]

def human_(opposition, strategies=strategies,
                   rounds=20):
    strategy_range = range(len(strategies))
    weights = [1] * len(strategies)
    bot = [], player = [], cum_score = 0
    print(range(rounds))
    for trial in range(rounds):
        bot_m_all = [strategy(bot, player) for strategy in strategies]
        i = choices(strategy_range, weights)[0]
        bot_m = bot_m_all[i]
        player_m = opposition(player, bot)

        score = scorer[bot_m + player_m]
        print(f'{bot_m} ~ {player_m} = {score:+d}'
            f'\t\t{strategies[i].__name__}')
        cum_score += score

        bot.append(bot_m)
        player.append(player_m)
        for i, bot_m in enumerate(bot_m_all):
            if scorer[bot_m + player_m] == 1:
                weights[i] += 1
        
    print('Total score:', cum_score)

if __name__ == '__main__':
    def human(bot, player):
        return input(f'Choose one of {rps!r}: ')

    human_(opposition=human, rounds=20)
