import random
play = True
x = random.randint(0,9)
while play:
    numb = int(input('enter a number from 0 to 9: '))
    if numb == x:
        print('u have guessed correctly... congrats!')
        break
    else:
        print('not quite... pls try again.')