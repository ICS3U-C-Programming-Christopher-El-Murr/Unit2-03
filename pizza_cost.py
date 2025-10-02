#!.usr/bin/env python3
# Created by Christopher El-Murr
# Created on Oct,1,2025
# This program calculated the cost of a pizza with tax
# after asking the user for the diameter
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches):"))

    # process
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * diameter
    total = subtotal + tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "__main__":
    main()