board = """
. . . . . . | . . . . . .
. . . . . . | . . . . . .
. . . . . . | . . . . . .
. . . . . . | . . . . . .
. . . . . . | . . . . . .
-------------------------
. . . . . . | . . . . . .
. . . . . . | . . . . . .
. . . . . . | . . . . . .
. . . . . . | . . . . . .
. . . . . . | . . . . . .
"""

white = "X"
black = "0"

empty_bar = """|
|
|
|
|"""

black_bar = empty_bar
white_bar = empty_bar

def combine_pip(pip_list):
    split_pips = [x.split("\n") for x in pip_list]
    out = []
    for x in split_pips:
        if out == []: 
            out = x
            continue
        out = [" ".join(y) for y in zip(out, x)]
        
    return out

empty_pip = """.
.
.
.
."""
pips = {}
for i in range(24):
    pips[i+1] = empty_pip
    
pip_order_top = [
    pips[13],
    pips[14],
    pips[15],
    pips[16],
    pips[17],
    pips[18],
    black_bar,
    pips[19],
    pips[20],
    pips[21],
    pips[22],
    pips[23],
    pips[24],
]

pip_order_bottom = [
    pips[12],
    pips[11],
    pips[10],
    pips[9],
    pips[8],
    pips[7],
    white_bar,
    pips[6],
    pips[5],
    pips[4],
    pips[3],
    pips[2],
    pips[1],
]

def print_board():
    for i in combine_pip(pip_order_top):
        print(i)
    print("-"*25)
    for i in combine_pip(pip_order_bottom):
        print(i)