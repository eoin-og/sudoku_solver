import timeit
import time

input_sudoku =    [[0,0,0,0,8,9,7,0,0],
                  [1,0,0,0,4,0,0,0,9],
                  [0,0,0,0,0,5,0,6,8],
                  [0,0,6,3,0,0,1,0,0],
                  [5,8,0,0,0,0,0,0,0],
                  [0,0,1,0,0,4,9,0,0],
                  [0,7,0,6,0,0,2,0,0],
                  [0,0,0,0,0,0,0,0,3],
                  [0,9,0,0,0,3,0,0,0]]

def valid_move(sudoku, i, j, target):
    #checks if target move is okay

    top_corner_x = 3 *int(i/3)
    top_corner_y = 3 *int(j/3)
    if all([target != sudoku[i][x] for x in range(9)]):                
            if all([target != sudoku[x][j] for x in range(9)]):                    
                    for x in range(top_corner_x, top_corner_x+3):
                            for y in range(top_corner_y, top_corner_y+3):
                                    if sudoku[x][y] == target:
                                            return False
                    return True
    return False

def next_cell(sudoku, i, j, first_pass=True):
    #fins next empty cell
    for x in range(i,9):
            for y in range(j,9):
                    if sudoku[x][y] == 0:
                            return x,y
    if first_pass:
         return next_cell(sudoku, 0, 0, False)

    #no more cells
    return -1,-1

def solve(sudoku, i,j):
        #moves through sudoku trying out every value, if there's a problem it back tracks

        i,j = next_cell(sudoku, i, j)
        if i == -1:
            return True
        
        for target in range(1,10):
            if valid_move(sudoku, i, j ,target):
                    sudoku[i][j] = target
                    if solve(sudoku, i, j):
                            return True
                    #back track
                    sudoku[i][j] = 0
        return False

print("----------------------------------\n Input:")
[print (row) for row in input_sudoku]
start_time = timeit.default_timer()
if solve(input_sudoku,0,0):
    end_time = timeit.default_timer()
    print("----------------------------------\n Solution:")
    [print (row) for row in input_sudoku]
    print("Time taken: "+str(end_time - start_time)+" seconds")
else: print ("NO SOLUTION FOUND")
