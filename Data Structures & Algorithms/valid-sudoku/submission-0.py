class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)       # key: value, val should be 1 for keys 1-9
        cols = defaultdict(set)          # key: value, val should be 1 for keys 1-9
        squares = defaultdict(set)       # key: value, key  = (r/3, c/3)

        for r in range(9):
            for c in range (9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[r//3, c//3]):
                   return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True