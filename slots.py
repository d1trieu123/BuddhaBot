
from random import choice

def play_slots():
    symbols = ['🍒', '🍋', '🍉']  
    result = ' '.join(choice(symbols) for _ in range(3))
    if result[0] == result[2] == result[4]:
        return f'Slots: {result} JACKPOT!'
    else:
     return f'Slots: {result}'