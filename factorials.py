#!/usr/bin/env python3
# Created By: Keiden
# Date: 2 / 2 / 2022
# This program calculates the factorial of any inputted number.


def main():
    print("Hi! insert a number, and this program will calculate that number's"
          " factorial.")

    starting_num = input(">")
    print()

    try:
        starting_num_int = int(starting_num)
        counter = starting_num_int
        final_num = 1

        while counter > 0:
            final_num = final_num * counter
            counter = counter - 1

        print("Your final number is", str(final_num) + "!")

    except ValueError:
        print("Invalid input!")


if __name__ == "__main__":
    main()
