import random

print('Welcome to the RPS Game')

CPUScore = 0
PlayerScore = 0
TieScore = 0

listOfOptions = ['Rock', 'Paper', 'Scissors']

def Winner(Cpu, Player):
    if(Player == 'Rock' and Cpu == 'Paper'):
        print('Sorry User, You Lost')
        return 'CPU'
    elif(Player == 'Rock' and Cpu == 'Scissors'):
        print('Congrats, You just won')
        return 'PLayer'
    elif(Player == 'Paper' and Cpu == 'Scissors'):
        print('Sorry User, You Lost')
        return 'CPU'
    elif(Player == 'Paper' and Cpu == 'Rock'):
        print('Congrats, You just won')
        return 'PLayer'
    elif(Player == 'Scissors' and Cpu == 'Paper'):
        print('Congrats, You just won')
        return 'PLayer'
    elif(Player == 'Scissors' and Cpu == 'Rock'):
        print('Sorry User, You Lost')
        return 'CPU'
    else:
        print('Sorry, It was a tie. Please try again')
        return 'Tie'

    

    
while (PlayerScore != 2 and CPUScore != 2):
    while True:
        Player = input('Make a choice: Rock, Paper, Scissors ')
        if(Player == 'Rock' or Player == 'Paper' or Player == 'Scissors'):
            break
        else:
            print('Invalid Option. Please try again.')

    Cpu = random.choice(listOfOptions)

    print('Your Input ', Player)
    print('Computer Input ', Cpu)
    result = Winner(Cpu, Player)

    if (result == 'PLayer'):
        PlayerScore += 1
    elif (result == 'CPU'):
        CPUScore += 1
    else:
        TieScore += 1
    print('Your Score ', PlayerScore, 'CPU Score ', CPUScore, 'Ties ', TieScore)
else:
    print('Game Over. Start Afresh')    
