'''
Snakes and Ladders simulation, because I was curious if this was actually random
or not. The results will shock you!

May right a paper on this or something, I don't know. Something something game
theory.
'''
from random import randint
from datetime import datetime

TRIALS = int(1e4)
WIN_TILE = 100
PLAYERS = 10
mappings = {n: n for n in range(1, WIN_TILE + 1)}
win_times = [0 for _ in range(PLAYERS)]

# Random seed
random.seed(datetime.now())

def roll():
    '''
    Roll the preverbial die
    '''
    return randint(1, 6)

def read_map_from_file(fn):
    '''
    Read the mappings for a snakes and ladders board from a file. Each line is
    formatted as follows:

    <starting_tile> <ending_tile>
    '''
    f = open(fn, 'r')
    for l in f.readlines():
        s, e = map(int, l.rstrip().split())
        mappings[s] = e
    f.close()

def print_winnings(winnings):
    for i, w in enumerate(winnings, 1):
        print("Player %02d: %d times" % (i, w))

read_map_from_file("map.txt")

for t in range(TRIALS):
    # Print status
    print("Trial %04d...\r" % (t + 1), end="")
    # Everyone starts out on square one
    ps = [0 for _ in range(PLAYERS)]
    turn = 0

    while not any(map(lambda x: x == WIN_TILE, ps)):
        # Roll it
        hypo_pos = ps[turn % PLAYERS] + roll()
        if hypo_pos > WIN_TILE:
            ps[turn % PLAYERS] = mappings[WIN_TILE - (hypo_pos - WIN_TILE)]
        else:
            ps[turn % PLAYERS] = mappings[hypo_pos]

        turn += 1

    win_times[ps.index(WIN_TILE)] += 1

print()
print_winnings(win_times)
