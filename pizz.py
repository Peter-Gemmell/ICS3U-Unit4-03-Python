#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program calculates the circumference of a circle using constants

def main():
    # this function calculates square exponents
    answer = 0
    number_squared = 0

    # input
    integer_input_string = input("Enter a positive integer: ")

    # process & output
    try:
        integer_input = int(integer_input_string)

        if integer_input >= 0:
            for number_squared in range(integer_input + 1):
                answer = number_squared * number_squared
                print("{0}² = {1}".format(number_squared, answer))
        else:
            print("Sorry, this program only accepts positive integers.")

    except Exception:
        print("Sorry, that is not a valid integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()