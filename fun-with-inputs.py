#!/usr/bin/python3
"""
Just testing out advance inputs from the pyinputplus module
"""

import pyinputplus as pyip

def main():
    myinputstr = pyip.inputMenu(['a', 'b', 'c'], prompt='Choisis mon gros…\n')
    print(f'Your choise is {myinputstr}.')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
