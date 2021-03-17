import pyinputplus as pyip

def main():
    response = 'yes'
    while response is not 'no':
        response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?\n')
    print('Ok, bye')   
        

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
