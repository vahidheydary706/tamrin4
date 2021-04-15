import time


def show():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=' ')
        print()

def win1():
    if game [0] [0] =='x' and game [0] [1] =='x' and game [0] [2] =='x':
        print('player1 wins')
        exit()
        
    elif game [1] [0] =='x' and game [1] [1] =='x' and game [1] [2] =='x':
        print('player1 wins')
        exit()

    elif game [2] [0] =='x' and game [2] [1] =='x' and game [2] [2] =='x':
        print('player1 wins')
        exit()

    elif game [0] [0] =='x' and game [1] [0] =='x' and game [2] [0] =='x':
        print('player1 wins')
        exit()

    elif game [0] [1] =='x' and game [1] [1] =='x' and game [2] [1] =='x':
        print('player1 wins')
        exit()

    elif game [0] [2] =='x' and game [1] [2] =='x' and game [2] [2] =='x':
        print('player1 wins')
        exit()

    elif game [0] [0] =='x' and game [1] [1] =='x' and game [2] [2] =='x':
        print('player1 wins')
        exit()

    elif game [0] [2] =='x' and game [1] [1] =='x' and game [2] [0] =='x':
        print('player1 wins')
        exit()
    print(f'time: {a}')

def win2():
    if game [0] [0] =='o' and game [0] [1] =='o' and game [0] [2] =='o':
        print('player2 wins')
        exit()
        
    elif game [1] [0] =='o' and game [1] [1] =='o' and game [1] [2] =='o':
        print('player2 wins')
        exit()

    elif game [2] [0] =='o' and game [2] [1] =='o' and game [2] [2] =='o':
        print('player2 wins')
        exit()

    elif game [0] [0] =='o' and game [1] [0] =='o' and game [2] [0] =='o':
        print('player2 wins')
        exit()

    elif game [0] [1] =='o' and game [1] [1] =='o' and game [2] [1] =='o':
        print('player2 wins')
        exit()

    elif game [0] [2] =='o' and game [1] [2] =='o' and game [2] [2] =='o':
        print('player2 wins')
        exit()

    elif game [0] [0] =='o' and game [1] [1] =='o' and game [2] [2] =='o':
        print('player2 wins')
        exit()

    elif game [0] [2] =='o' and game [1] [1] =='o' and game [2] [0] =='o':
        print('player2 wins')
        exit()
    print(f'time: {a}')

game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

show()

while True:
    a = time.time()


    # player1
    print('player1')
    while True:
        row = int(input())
        col = int(input())
        
        if 0 <= row <= 2 and 0 <=  col <= 2:
            if game[row] [col] == '_':
                game[row] [col] = 'x'
                break
            else:
                print('Error!!! try again')
        else:
            print('Error!!! try again')
    show()
    win1()
    # player2
    print('player2')
    while True:
        row = int(input())
        col = int(input())
        
        if 0 <= row <= 2 and 0 <=  col <= 2:
            if game[row] [col] == '_':
                game[row] [col] = 'o'
                break
            else:
                print('Error!!! try again')
        else:
            print('Error!!! try again')
    show()
    win2()
    