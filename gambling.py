import random
import matplotlib.pyplot as plt

# Roulette betting; colors only
def roulette(bet, color, spins):
    x = []
    y = []
    wheel = ['red']*18 + ['black']*18 + ['green']*2
    winnings = 0
    restore_bet = bet
    for spin in range(0, spins):
        rand = random.choice(wheel)
        if color == rand:
            winnings = winnings + bet
            bet = restore_bet
            x.append(spin)
            y.append(winnings)
        else:
            winnings = winnings - bet
            bet = bet*2
            x.append(spin)
            y.append(winnings)
    plt.plot(x,y)
    plt.show()
    return winnings


print(roulette(1, 'red', 100))
