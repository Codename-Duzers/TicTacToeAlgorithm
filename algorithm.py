winTrigger = 0
piece = 0

squareToCoord = {'A1': [0,0], 'B1': [0,1], 'C1': [0,2], 'A2': [1,0], 'B2': [1,1], 'C2': [1,2], 'A3': [2,0], 'B3': [2,1], 'C3': [2,2]}

gameBoard = [['A1', 'B1', 'C1'],
             ['A2', 'B2', 'C2'],
             ['A3', 'B3', 'C3']]

playedMoves = []

piece = int(input('Who is the starting player? (Input 1 or 0)'))

def winChecker(board):
    win = False
    oneTracker = 0
    zeroTracker = 0
    for i in range(len(board[0])):
        if board[0][i] == int(1):
            oneTracker = oneTracker + 1
        if board[0][i] == int(0):
            zeroTracker = zeroTracker + 1
        if oneTracker == 3 or zeroTracker == 3:
            win = True
            break
    return win
        
while winTrigger == 0:
    raw_move = input('What position would you like to play?')
    
    if raw_move in squareToCoord.items() == False:
        print("This value is outside the scope of the board")
        continue     
    elif raw_move in playedMoves:
        print("Sorry, this move has alredy been played, please select another spot")
        continue
    else:
        proc_move = squareToCoord.get(raw_move)
        gameBoard[proc_move[0]][proc_move[1]] = piece
        playedMoves.append(raw_move)
        piece = piece * -1 + 1
        winChecker(gameBoard)
        
    print(winChecker(gameBoard))
    print(gameBoard)