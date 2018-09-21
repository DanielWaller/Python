# Chess on Python 2

import string

chessBoard = [[1]*9 for i in range(9)]
# 0th row and column are ignored for ease of notation

files = string.ascii_lowercase[:8]
xInd_to_fileInd = {num: char for (num,char) in zip(range(1,9),files)}
fileInd_to_xInd = {char: num for (char,num) in zip(files,range(1,9))}

def getKnightMoves(square, chessBoard):
	# A function to return all knight moves on the board from the given square.
	xInd = fileInd_to_xInd[square[0]]
	yInd = square[1]
	i,j = xInd,int(yInd)
	possibleMoves = []
	
	# Add all 8 possible moves
	possibleMoves.append([i+1,j+2])
	possibleMoves.append([i+1,j-2])
	possibleMoves.append([i-1,j+2])
	possibleMoves.append([i-1,j-2])
	possibleMoves.append([i+2,j+1])
	possibleMoves.append([i-2,j+1])
	possibleMoves.append([i+2,j-1])
	possibleMoves.append([i-2,j-1])
	
	# Filter those which end up off the board
	
	# Filter those square occupied by pieces of same colour
	
	# Pass moves back
	return(possibleMoves)
	
def getRookMoves(square, chessBoard):
    # A function to return all rook moves on the board from the given square.
    xInd = fileInd_to_xInd[square[0]]
    yInd = square[1]
    i,j = xInd,int(yInd)
    possibleMoves = []
    
    # Add all moves on the same file
    possibleFileMoves = [1,2,3,4,5,6,7,8]
    possibleFileMoves.remove(j)
    for a in possibleFileMoves:
        possibleMoves.append([i,a])
    
    # Add all possible moves on the same rank
    possibleRankMoves = [1,2,3,4,5,6,7,8]
    possibleRankMoves.remove(i)
    for a in possibleRankMoves:
        possibleMoves.append([a,j])
    
    # Filter those squares occupied or beyond pieces of same colour
    
    # Pass moves back
    return(possibleMoves)
    
def getKingMoves(square, chessBoard):
    # A function to return all king moves on the board from the given square
    xInd = fileInd_to_xInd[square[0]]
    yInd = square[1]
    i,j = xInd,int(yInd)
    possibleMoves = []
    
        # Add all 8 possible moves
    possibleMoves.append([i+1,j])
    possibleMoves.append([i-1,j])
    possibleMoves.append([i,j+1])
    possibleMoves.append([i,j-1])
    possibleMoves.append([i+1,j+1])
    possibleMoves.append([i-1,j+1])
    possibleMoves.append([i+1,j-1])
    possibleMoves.append([i-1,j-1])
	
    # Filter those which end up off the board
	
    # Filter those square occupied by pieces of same colour
	
    # Pass moves back
    return(possibleMoves)

def getBishopMoves(square, chessBoard):
    # A function to return all bishop moves on the board from the given square
    xInd = fileInd_to_xInd[square[0]]
    yInd = square[1]
    i,j = xInd,int(yInd)
    possibleMoves = []
    
    # Add all moves going NE until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp <= 7 and j_temp <= 7:
        i_temp,j_temp = i_temp + 1, j_temp + 1
        possibleMoves.append([i_temp,j_temp])
    
    # Add all moves going NW until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp >= 2 and j_temp <= 7:
        i_temp,j_temp = i_temp - 1, j_temp + 1
        possibleMoves.append([i_temp,j_temp])
        
    # Add all moves going SE until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp <= 7 and j_temp >= 2:
        i_temp,j_temp = i_temp + 1, j_temp - 1
        possibleMoves.append([i_temp,j_temp])
    
    # Add all moves going SW until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp >= 2 and j_temp >= 2:
        i_temp,j_temp = i_temp - 1, j_temp - 1
        possibleMoves.append([i_temp,j_temp])
        
    # Return all possible moves
    return(possibleMoves)
    
def getQueenMoves(square, chessBoard):
    # A function to return all queen moves on the board from the given square
    xInd = fileInd_to_xInd[square[0]]
    yInd = square[1]
    i,j = xInd,int(yInd)
    possibleMoves = []
    
    # Add all moves going NE until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp <= 7 and j_temp <= 7:
        i_temp,j_temp = i_temp + 1, j_temp + 1
        possibleMoves.append([i_temp,j_temp])
        
    # Add all moves going N until we hit the board edge
    i_temp, j_temp = i,j
    while j_temp <= 7:
        i_temp,j_temp = i_temp, j_temp + 1
        possibleMoves.append([i_temp,j_temp])
    
    # Add all moves going NW until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp >= 2 and j_temp <= 7:
        i_temp,j_temp = i_temp - 1, j_temp + 1
        possibleMoves.append([i_temp,j_temp])
        
    # Add all moves going W until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp >= 2:
        i_temp,j_temp = i_temp - 1, j_temp
        possibleMoves.append([i_temp,j_temp])
        
    # Add all moves going SE until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp <= 7 and j_temp >= 2:
        i_temp,j_temp = i_temp + 1, j_temp - 1
        possibleMoves.append([i_temp,j_temp])
        
    # Add all moves going E until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp <= 7:
        i_temp,j_temp = i_temp + 1, j_temp
        possibleMoves.append([i_temp,j_temp])
    
    # Add all moves going SW until we hit the board edge
    i_temp, j_temp = i,j
    while i_temp >= 2 and j_temp >= 2:
        i_temp,j_temp = i_temp - 1, j_temp - 1
        possibleMoves.append([i_temp,j_temp])
        
    # Add all moves going S until we hit the board edge
    i_temp, j_temp = i,j
    while j_temp >= 2:
        i_temp,j_temp = i_temp, j_temp -1
        possibleMoves.append([i_temp,j_temp])
        
    # Return all possible moves
    return(possibleMoves)
    
def getWhitePawnMoves(square, chessBoard):
    # Return all possible pawn moves (pawn is White)
    xInd = fileInd_to_xInd[square[0]]
    yInd = square[1]
    i,j = xInd,int(yInd)
    possibleMoves = []
    
    # Add all moves advancing one square forward
    possibleMoves.append([i,j+1])
    
    # Add the move 2 squares forward if the rank number is 2
    if (j== 2):
        possibleMoves.append([i,4])
        
    # Add normal captures
    
    # Add en passant captures
    
    # Return all possible moves
    return(possibleMoves)

def getBlackPawnMoves(square, chessBoard):
    # Return all possible pawn moves (pawn is Black)
    xInd = fileInd_to_xInd[square[0]]
    yInd = square[1]
    i,j = xInd,int(yInd)
    possibleMoves = []
    
    # Add all moves advancing one square forward
    possibleMoves.append([i,j-1])
    
    # Add the move 2 squares forward if the rank number is 2
    if (j== 7):
        possibleMoves.append([i,5])
        
    # Add normal captures
    
    # Add en passant captures
    
    
    # Return all possible moves
    return(possibleMoves)

print("Square?")
square = raw_input()
possibleMoves = getWhitePawnMoves(square, chessBoard)
print len(possibleMoves)
print(possibleMoves)
	
	

