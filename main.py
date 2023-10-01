from boardmaker import BoardMaker
import pygame

board = [
    [8,0,0,7,0,3,1,0,4],
    [0,0,0,0,0,0,0,7,0],
    [0,0,9,2,0,0,0,0,0],
    [4,0,0,0,0,1,6,0,3],
    [0,0,0,0,0,0,0,0,5],
    [0,8,0,0,4,0,0,0,0],
    [0,2,0,3,0,0,7,0,6],
    [6,0,0,0,0,0,0,5,0],
    [0,0,0,0,0,7,0,8,0]
]

#board2 = BoardMaker()

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = " ")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = " ")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0: # if empty
                return (i, j) # row, col
    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: # if num is in row and not in the same position
            return False
    
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i: # if num is in column and not in the same position
            return False
    
    # Check box
    box_x = pos[1] // 3 # integer division
    box_y = pos[0] // 3 # integer division

    for i in range(box_y * 3, box_y * 3 + 3): # loop through rows
        for j in range(box_x * 3, box_x * 3 + 3): # loop through columns
            if bo[i][j] == num and (i, j) != pos: # if num is in box and not in the same position
                return False
    
    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False


"""create a gui for this soduku solver in pygame"""



if __name__ == "__main__":
    
    print("\n")
    print("Unsolved board: ")
    print_board(board)
    print("\n")
    print("Solving...")
    print("\n")
    print("Solved board: ")
    solve(board)
    print_board(board)