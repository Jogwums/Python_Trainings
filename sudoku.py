def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None 

def is_valid(puzzle, guess, row, col):

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #normal loop
    # col_vals = []  
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    
    col_vals = [puzzle[i][col] for i in range(9)] #recurssion 
    if guess in col_vals:
        return False 

    # then the square (3x3 square)
    row_start = ( row // 3) * 3 
    col_start = ( col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range ( col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    #else return True 
    return True 


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True 

    #if there's a place to put a number, make a guess btw 1 and 9 
    for guess in range(1, 10):
        
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True 


        #if guess was wrong 
        puzzle[row][col] = -1 #reset the guess

    #if puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = []

    print(solve_sudoku(example_board))
    print(example_board)
    
