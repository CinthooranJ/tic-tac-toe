print("You're playing Tic-Tac-Toe! This game uses a 3x3 grid, the x coordinates are listed as A,B,C and y coordinates as 1,2,3. Enter these coordinates to play your turn! Good Luck!")

player = "X"
board = {"A1": " ", "B1": " ", "C1": " ",
         "A2": " ", "B2": " ", "C2": " ",
         "A3": " ", "B3": " ", "C3": " "} # Dictionary containing a blank value tied to a corresponding coordinate, to act as a board

def isTurnValid(x,y):
    if x == "A" or x == "B" or x == "C":
        if y == "1" or y == "2" or y == "3":
            if board[(x+y)] == " ":
                return True
    return False
    
def winCondition(player):
    if board["A1"] == board["B1"] == board["C1"] == player: # Checks all possible win conditions on the board, and returns true if there is.
        return True
    elif board["A2"] == board["B2"] == board["C2"] == player:
        return True
    elif board["A3"] == board["B3"] == board["C3"] == player:
        return True
    
    elif board["A1"] == board["A2"] == board["A3"] == player:
        return True
    elif board["B1"] == board["B2"] == board["B3"] == player:
        return True
    elif board["C1"] == board["C2"] == board["C3"] == player:
        return True

    elif board["A1"] == board["B2"] == board["C3"] == player:
        return True
    elif board["C1"] == board["B2"] == board["A3"] == player:
        return True
    return False
        
turns_number = 0 # Will go up each correct turn; Game will end in a tie after nine turns.
while True:
    print()
    print("Player",player,", enter your coordinates(Ex: A1, B2):")
    x,y = input()
    
    if isTurnValid(x,y) == True:
        coord = x + y
        board[coord] = player
        turns_number += 1
            
        if winCondition(player) == True:
            print("Hooray! Player",player,"is the winner!")
            break
        elif turns_number == 9:
            print("The game was unfortunately inconclusive...")
            break
    else:
        print("Turn is invalid, please try again.")
        continue
    
    #Player Alternation
    if player == "X":  
        player = "O"
    else:
        player = "X"
