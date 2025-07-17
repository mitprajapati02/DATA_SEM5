def fnPush():

def fnPop():

def fnDisplay():


def main():
    print('hello world')

    while (True):
        totalLength = int(input('Please Enter Length of List: \t'))
        if totalLength > 0:
            break
        else:
            print('Please Enter value more than 0')
    while (True):
        print('----Menu---')
        print('1) push')
        print('2) pop')
        print('3) display')
        print('4) exit')
        while (True):
            userChoice = int(input('Please Enter Selected Number: \t'))
            if userChoice < 5 and userChoice > 0:
                match userChoice:
                    case 1:
                        fnPush()
                    case 2:
                        fnPop()
                    case 3:
                        fnDisplay()
                    case 4:
                        return
            else:
                print('Please Select valid number from menu')
main()