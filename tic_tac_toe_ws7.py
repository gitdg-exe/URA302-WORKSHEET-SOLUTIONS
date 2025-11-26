def print_board(b):
    for i in range(0,9,3):
        print(b[i]+'|'+b[i+1]+'|'+b[i+2])
    print()

def check_winner(b,p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,c,d in wins:
        if b[a]==b[c]==b[d]==p:
            return True
    return False

def check_tie(b):
    return all(x!=' ' for x in b)

def get_player_input(p,b):
    while True:
        try:
            pos=int(input(f"{p} enter position 1-9:\""))-1
            if pos<0 or pos>8: print("invalid"); continue
            if b[pos]!=' ': print("taken"); continue
            return pos
        except:
            print("invalid")

def play_game():
    board=[' ']*9
    player='X'
    while True:
        print_board(board)
        pos=get_player_input(player,board)
        board[pos]=player
        if check_winner(board,player):
            print_board(board)
            print(player,'wins')
            break
        if check_tie(board):
            print_board(board)
            print('Tie')
            break
        player = 'O' if player=='X' else 'X'
    if input('Play again? y/n:').lower().startswith('y'):
        play_game()

if __name__=='__main__':
    play_game()
