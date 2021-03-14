#!/usr/bin/python3
"""
Fun with tables of text
"""

__author__ = "Philippe Lemaire"


def main():
    """ Main entry point of the app """
    printTable(tableData)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    """prints a pretty table from a list of lists of strings"""
    colWidth = [0]*len(table)

    for i in range(len(table)):
        maxLength = 0
        for word in table[i]:

            if len(word) > maxLength:
                maxLength = len(word)
        colWidth[i] = maxLength

    for i in range(len(table[0])):
        print(table[0][i].rjust(colWidth[0]), table[1][i].rjust(
            colWidth[1]), table[2][i].rjust(colWidth[2]))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
