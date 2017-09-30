# Snakes and Ladders Simulation

A very crude and hastily made simulation of the all-time favourite childhood
game. Plays multiple trials (games) with a variable number of players, and
stores the number of wins per player. Shows results after running.

Tile mappings are based off of an actual Snakes and Ladders board that I have
sitting in front of me - "Snakes & Ladders (Magnetic Game) No. 222".

# How to Play

[Here](https://en.wikipedia.org/wiki/Snakes_and_Ladders#Gameplay).

# How to Simulate

```sh
python main.py
```

# How to Customize

Edit the `main.py` file directly. There are 3 constants that you can readily
change: `TRIALS`, `WIN_TILE`, and `PLAYERS`.

Editing the `map.txt` file will change the tile mappings. Format per line is as
follows:

```
<start> <end>
```

Where `<start>` is the place that the trap/ladder will reside, and `<end>` is
where the player will end up, after the player lands on it.

#### TRIALS

The number of trials to be run. The larger the number, the more statistically
significant the results will be.

#### WIN_TILE

The tile which triggers the win condition. The larger the number, the longer the
game, and vice versa. Recommended to be set at `100`, as reminiscent to the
classic good-ole game.

#### PLAYERS

The number of players playing the game. Just as a note, that Player 1 always
goes first, no matter what, and then goes Player 2, and then Player 3, and so
on.

# Quirks

The win condition is a family rule. You must roll the exact number necessary for
winning in order to win. Not doing such will result in going to the final square
and back again. In certain circumstances, it will make the player get further
away from the final square.

If the player rolls a 6, the player does not get another turn. Though that could
also be easily added.
