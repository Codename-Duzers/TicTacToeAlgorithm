WinTrigger = 0
PieceTypeTrigger = True
Piece = 0

Dict = {'1': [0,0], '2': [0,1], '3': [0,2], '4': [1,0], '5': [1,1], '6': [1,2], '7': [2,0], '8': [2,1], '9': [2,2]}

GameBoard = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

PlayedMoves = []

Piece = int(input("Who is the starting player? (Input 1 or 0)"))

while WinTrigger == 0:
    raw_move = input("What position would you like to play?")
    
    if int(raw_move[0]) < 1 or int(raw_move[0]) > 9:
        print("This value is outside the scope of the board")
        continue     
    elif raw_move in PlayedMoves:
        print("Sorry, this move has alredy been played, please select another spot")
        PlayedMoves.append(raw_move)
        continue
    else:
        proc_move = Dict.get(raw_move)
        GameBoard[proc_move[0]][proc_move[1]] = Piece
        PlayedMoves.append(raw_move)
        Piece = Piece * -1 + 1
    
    print(GameBoard)