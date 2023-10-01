winTrigger = False
piece = 0
visualpiece = 0

squareToCoord = {'A1': [0,0], 'B1': [0,1], 'C1': [0,2], 'A2': [1,0], 'B2': [1,1], 'C2': [1,2], 'A3': [2,0], 'B3': [2,1], 'C3': [2,2]}

gameBoard = [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']]

playedMoves = []

initialPiece = (input('Who is the starting player? (Input X or O)'))

if initialPiece == 'X':
    piece = 1
elif initialPiece == 'O':
    piece = 0

def winChecker(board):
    win = False
    #Diag-onal Check T-op B-ottom 1-Piece one (and vice versa)
    diagCheckTB1 = 0
    diagCheckBT1 = 0
    
    diagCheckTB0 = 0
    diagCheckBT0 = 0
    #Horizontal and Vertical Checking
    for y in range(len(board)):
        horZoneTracker = 0
        horZeroTracker = 0
        for h in range(len(board[y])):
            if board[y][h] == str('X') + ' ':
                horZoneTracker = horZoneTracker + 1
            if board[y][h] == str('O') + ' ':
                horZeroTracker = horZeroTracker + 1
            if horZoneTracker == 3 or horZeroTracker == 3:
                win = True
                break
        
        vertOneTracker = 0
        vertZeroTracker = 0
        for v in range(len(board[y])):
            if board[v][y] == str('X') + ' ':
                vertOneTracker = vertOneTracker + 1
            if board[v][y] == str('O') + ' ':
                vertZeroTracker = vertZeroTracker + 1
            if vertOneTracker == 3 or vertZeroTracker == 3:
                win = True
                break
            
        #Diagonal Checking
        if board[y][y] == str('X') + ' ':
            diagCheckTB1 = diagCheckTB1 + 1
        if board[y][y] == str('O') + ' ':
            diagCheckTB0 = diagCheckTB0 + 1
            
        if board[-y + 2][y] == str('X') + ' ':
            diagCheckBT1 = diagCheckBT1 + 1
        if board[-y + 2][y] == str('O') + ' ':
            diagCheckBT0 = diagCheckBT0 + 1
            
        if diagCheckTB1 == 3 or diagCheckTB0 == 3 or diagCheckBT1 == 3 or diagCheckBT0 == 3:
                win = True
                break
    return win
        
while winTrigger == False:
    raw_move = input('What position would you like to play?')
    
    if raw_move in squareToCoord.items() == False:
        print("This value is outside the scope of the board")
        continue     
    elif raw_move in playedMoves:
        print("Sorry, this move has alredy been played, please select another spot")
        continue
    else:
        proc_move = squareToCoord.get(raw_move)
        if piece == 0:
            visualpiece = 'O'
        elif piece == 1:
            visualpiece = 'X'
        gameBoard[proc_move[0]][proc_move[1]] = str(visualpiece) + ' '
        playedMoves.append(raw_move)
        piece = piece * -1 + 1
        if winChecker(gameBoard) == True:
            winTrigger = True
        
    for x, y, z in zip(*gameBoard):
        print(x, y, z)
        
    #print(winChecker(gameBoard))

print('Congratulations, you WON!')