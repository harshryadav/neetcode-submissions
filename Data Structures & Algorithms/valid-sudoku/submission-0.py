class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):

                if board[r][c] == ".":
                    continue

                square = (r // 3) * 3 + (c // 3)

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sub_squares[square]:
                    print("returning false for: ", board[r][c])
                    return False
            
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub_squares[square].add(board[r][c])
        
        return True

'''
create three hash sets for rows, columns, and each of the 3x3 squares
We go through the matrix
    if the current row, col is a "." then we ignore
    
    calculate which square the row, col falls in
    
    if one of the three conditions is violated
        return false
    
    we add the value to the sets
   
return true



[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


rows=
0 -> 1,2,3
1 -> 4,5
2 -> 9,1,3
3 -> 5,6,4
4 -> 8,3,5
5 -> 7,2,6
6 -> 2
7 -> 4,1,9,8
8 -> 8,7,9

cols=
0 -> 1,4,5,7
1 -> 2,9
2 -> 1
3 -> 5,8,4
4 -> 3,6,2,1,8
5 -> 3,9
6 -> 2
7 -> 7
8 -> 3,4,5,6,8,9



'''