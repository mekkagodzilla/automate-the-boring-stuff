#!/usr/bin/python3
"""
Fantasy Game Inventory
"""

__author__ = "Philippe Lemaire"


def main():
    """ Main entry point of the app """
    displayInventory(sampleInventory)
    addToInventory(sampleInventory, dragonLoot)
    displayInventory(sampleInventory)


def displayInventory(inventory):
    """Displays inventory as nicely as possible"""
    totalItems = 0
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
        totalItems += value
    print("\nTotal number of items:", totalItems)


sampleInventory = {'rope': 1, 'torch': 6,
                   'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    """takes a dict and a list and adds up the items in the list to the dict"""
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
