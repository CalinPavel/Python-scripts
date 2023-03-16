#!/usr/bin/env python
"""
A command-line controlled coffee maker.
"""

import sys
import load_recipes

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

def help():
    for string in commands:
        print(string)

def list():
    for string in load_recipes.recipes:
        print(string['name'])

def make_coffee():
    type=input("What kind of coffee?\n")
    for string in load_recipes.recipes:
        if string['name'] == type and string['water'] < RESOURCES[WATER] and  string['coffee'] < RESOURCES[COFFEE] and string['milk'] < RESOURCES[MILK]:
            print('done!')
            RESOURCES[WATER]-=string['water']
            RESOURCES[MILK]-=string['milk']
            RESOURCES[COFFEE]-=string['coffee']


def show():
    for string in RESOURCES:
        print( string , RESOURCES[string])

def refill():
    for string in RESOURCES:
        RESOURCES[string] = 100


def main():
    print("I'm a simple coffee maker")
print("Press enter")

while True:
    line=input("Insert command:")
    if line == 'exit' :
        break

    if line == 'list':
        list()

    if line == 'make':
        make_coffee()

    if line == 'status':
        show()

    if line == 'refill':
        refill()

    if line == 'help':
        help()



if __name__ == '__main__':
    main()





