import random

# Roulette betting; colors only
def roulette(bet, color, spins):
    wheel = ['red']*18 + ['black']*18 + ['green']*2
    winnings = 0
    restore_bet = bet
    for spin in range(0, spins):
        print(winnings)
        rand = random.choice(wheel)
        if color == rand:
            winnings = winnings + bet
            bet = restore_bet
        else:
            winnings = winnings - bet
            bet = bet*2
    return winnings


print(roulette(2, 'red', 100))
