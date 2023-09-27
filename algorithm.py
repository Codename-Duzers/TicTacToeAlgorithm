WinTrigger = 0
Piece = 0

Dict = {'A1': [0,0], 'B1': [0,1], 'C1': [0,2], 'A2': [1,0], 'B2': [1,1], 'C2': [1,2], 'A3': [2,0], 'B3': [2,1], 'C3': [2,2]}

GameBoard = [['A1', 'B1', 'C1'],
             ['A2', 'B2', 'C2'],
             ['A3', 'B3', 'C3']]

PlayedMoves = []

Piece = int(input('Who is the starting player? (Input 1 or 0)'))

def winChecker(board):
    win = False
    rowEval = 0
    for x in board[0]:
        r1 = 0
        if board[0][r1] == 1:
            rowEval = rowEval + 1
            r1 = r1 + 1 
        if rowEval == 3:
            win = True
            break
    print(r1)
    return win
        
while WinTrigger == 0:
    raw_move = input('What position would you like to play?')
    
    if raw_move in Dict.items() == False:
        print("This value is outside the scope of the board")
        continue     
    elif raw_move in PlayedMoves:
        print("Sorry, this move has alredy been played, please select another spot")
        continue
    else:
        proc_move = Dict.get(raw_move)
        GameBoard[proc_move[0]][proc_move[1]] = Piece
        PlayedMoves.append(raw_move)
        Piece = Piece * -1 + 1
    
    print(winChecker(GameBoard))
    print(GameBoard)