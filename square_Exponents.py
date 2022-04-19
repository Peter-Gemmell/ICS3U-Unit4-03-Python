#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on April 2022
# This program calculates square exponents


def main():
    # this function calculates square exponents
    answer = 0
    number_squared = 0

    # input
    integer_input_string = input("Enter the integer you’d like to square: ")

    # process & output
    try:
        integer_input = int(integer_input_string)

        if integer_input >= 0:
            for number_squared in range(integer_input + 1):
                answer = number_squared * number_squared
                print("{0}² = {1}".format(number_squared, answer))
        else:
            print("Invalid, only positive integers accepted")

    except Exception:
        print("Invalid Integer, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
