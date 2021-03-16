#!/usr/bin/python3
"""
Phone and mail extractor

Say you have the boring task of finding every phone number and email address in a long web page or document. If you manually scroll through the page, you might end up searching for a long time. But if you had a program that could search the text in your clipboard for phone numbers and email addresses, you could simply press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard, and then run your program. It could replace the text on the clipboard with just the phone numbers and email addresses it finds.

Whenever you’re tackling a new project, it can be tempting to dive right into writing code. But more often than not, it’s best to take a step back and consider the bigger picture. I recommend first drawing up a high-level plan for what your program needs to do. Don’t think about the actual code yet—you can worry about that later. Right now, stick to broad strokes.

For example, your phone and email address extractor will need to do the following:

    Get the text off the clipboard.
    Find all phone numbers and email addresses in the text.
    Paste them onto the clipboard.

Now you can start thinking about how this might work in code. The code will need to do the following:

    Use the pyperclip module to copy and paste strings.
    Create two regexes, one for matching phone numbers and the other for matching email addresses.
    Find all matches, not just the first match, of both regexes.
    Neatly format the matched strings into a single string to paste.
    Display some kind of message if no matches were found in the text.

"""

__author__ = "Philippe Lemaire"

import pyperclip, re

def main():
    phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})       # dot-something
        )''', re.VERBOSE)


    text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += 'x' + groups[8]
        matches.append(phoneNum)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])



    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to the clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()