#!/usr/bin/python3
"""
Fantasy Game Inventory
"""

__author__ = "Philippe Lemaire"


def main():
    """ Main entry point of the app """
    displayInventory(sampleInventory)


def displayInventory(inventory):
    """Displays inventory as nicely as possible"""
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)


sampleInventory = {'rope': 1, 'torch': 6,
                   'gold coin': 42, 'dagger': 1, 'arrow': 12}

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
