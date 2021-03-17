''' Sandwitch maker
Write a program that asks users for their sandwich preferences.
The program should use PyInputPlus to ensure that they enter valid input:

- Using inputMenu() for a bread type: wheat, white, or sourdough.
- Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
- Using inputYesNo() to ask if they want cheese.
    If so, using inputMenu() to ask for a
    cheese type: cheddar, Swiss, or mozzarella.
- Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
- Using inputInt() to ask how many sandwitches they want.
    Make sure this number is 1 or more.

Come up with prices for each of these options,
and have your program display a total cost i
after the user enters their selection.
'''
import pyinputplus as pyip

breadOptions = {'wheat': 1.5, 'white': 1, 'sourdough': 2}

proteinOptions = {'chicken': 2, 'turkey': 2.5, 'ham': 3, 'tofu': 3}

cheeseOptions = {'cheddar': 1, 'Swiss': 1.5, 'mozzarella': 2}

dressingOptions = {'mayo': 0.5, 'mustard': 0.5, 'lettuce': 1, 'tomato': 1}

totalValue = 0

print('Hello dear customer, what do you want to eat today?')

print('What kind of bread do you want?')
breadChoice = pyip.inputMenu(list(breadOptions.keys()))
print(f'You have selected {breadChoice}.')
totalValue += breadOptions[breadChoice]

print('What kind of protein do you want?')
proteinChoice = pyip.inputMenu(list(proteinOptions.keys()))
print(f'You have selected {proteinChoice}.')
totalValue += proteinOptions[proteinChoice]

cheeseWanted = pyip.inputYesNo('Do you want any cheese? [Yes/No]\n')

if cheeseWanted is 'yes':
    print('What kind of cheese do you want?')
    cheeseChoice = pyip.inputMenu(list(cheeseOptions.keys()))
    print(f'You have selected {cheeseChoice}.')
    totalValue += cheeseOptions[cheeseChoice]

dressingWanted = pyip.inputYesNo('Do you want any dressing? [Yes/No]\n')

if dressingWanted is 'yes':
    print('What kind of dressing do you want?')
    dressingChoice = pyip.inputMenu(list(dressingOptions.keys()))
    print(f'You have selected {dressingChoice}.')
    totalValue += dressingOptions[dressingChoice]

numberOfSandwitches = pyip.inputInt('How many sandwiches like this one?\n', min=1)
totalValue *= numberOfSandwitches

print(f'Your total is {totalValue} euros.')
