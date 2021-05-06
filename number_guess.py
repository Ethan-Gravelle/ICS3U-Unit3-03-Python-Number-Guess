#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: May 6, 2020
# This program is a guessing game

import random


def main():
    # this function is a guessing game
    # this generates a number between 1-9
    some_variable = random.randint(1, 9)

    # input
    number = int(input("Enter a number between 1-9: "))
    # process & output
    if number == some_variable:
        print("Correct")
    else:
        print("Incorrect")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
