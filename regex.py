import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNumRegex.search('My number is 511-398-2938.')
print('phone number found: ' + mo.group())



heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo1.group())
print(mo2.group())
