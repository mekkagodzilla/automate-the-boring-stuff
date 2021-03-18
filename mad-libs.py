import os
from pathlib import Path
import pyinputplus as pyip

a = 'adjective'.upper()
n = 'noun'.upper()
v = 'verb'.upper()

matches = [a, n, v]



with open('mad-libs-seed.txt', 'r') as seedFile:
    phrase = seedFile.read().split(' ')
    modifiedPhrase = []
    for word in phrase:
        if word in matches :
            userInput = pyip.inputStr(f'Please input a {word.lower()}.\n')
            modifiedPhrase.append(userInput)
        elif word[:-1] in matches:
            userInput = pyip.inputStr(f'Please input a {word[:-1].lower()}.\n')
            modifiedPhrase.append(userInput + '.')
        else:
            modifiedPhrase.append(word)

    finalPhrase = ' '.join(modifiedPhrase)
    print(finalPhrase)
