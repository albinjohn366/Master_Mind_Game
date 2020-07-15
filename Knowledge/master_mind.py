# MATER MIND PUZZLE

from my_logic_of_knowledge import *

# Adding colors available to color list
colors = ['red', 'blue', 'green', 'yellow']
symbols = []
knowledge = And()

# Adding symbols to the symbols list
for color in colors:
    for i in range(4):
        symbols.append(Symbol('{}_{}'.format(color, i)))

# Only one color and one position combination is available
for color in colors:
    knowledge.add(Or(Symbol('{}_1'.format(color)),
                     Symbol('{}_2'.format(color)),
                     Symbol('{}_3'.format(color)),
                     Symbol('{}_4'.format(color))))

# A single color can be in only there in one position
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(Implication(Symbol('{}_{}'.format(color, i)),
                                          Not(Symbol(
                                              '{}_{}'.format(color, j)))))

# A position could be occupied by only one color
for i in range(4):
    for color_1 in colors:
        for color_2 in colors:
            if color_1 != color_2:
                knowledge.add(Implication(Symbol('{}_{}'.format(color_1, i)),
                                          Not(Symbol(

                                              '{}_{}'.format(color_2, i)))))

# Representing the knowledge that we already know
knowledge.add(Or(
    And(Symbol("red_0"), Symbol("blue_1"), Not(Symbol("green_2")), Not(Symbol(
        "yellow_3"))),
    And(Symbol("red_0"), Symbol("green_2"), Not(Symbol("blue_1")), Not(Symbol(
        "yellow_3"))),
    And(Symbol("red_0"), Symbol("yellow_3"), Not(Symbol("blue_1")), Not(Symbol(
        "green_2"))),
    And(Symbol("blue_1"), Symbol("green_2"), Not(Symbol("red_0")), Not(Symbol(
        "yellow_3"))),
    And(Symbol("blue_1"), Symbol("yellow_3"), Not(Symbol("red_0")), Not(Symbol(
        "green_2"))),
    And(Symbol("green_2"), Symbol("yellow_3"), Not(Symbol("red_0")),
        Not(Symbol("blue_1")))
))

# Adding additional information to knowledge
knowledge.add(And(
    Not(Symbol("blue_0")),
    Not(Symbol("red_1")),
    Not(Symbol("green_2")),
    Not(Symbol("yellow_3"))
))

# Model checking for each symbol with the knowledge we know
for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol.symbols())