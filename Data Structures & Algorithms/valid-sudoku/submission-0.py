class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0]*9 for _ in range(9)]
        cols = [[0]*9 for _ in range(9)]
        for quadrant in range(9):
            arr = [0]*9
            for row in range((quadrant // 3) * 3, (quadrant // 3) * 3 + 3):
                for col in range((quadrant % 3) * 3, (quadrant % 3) * 3 + 3):
                    if board[row][col] != ".":
                        num = int(board[row][col])
                        if arr[num-1] == 1 or rows[row][num-1] == 1 or cols[col][num-1] == 1:
                            print(rows)
                            print(cols)
                            print(quadrant, row, col, num)
                            return False
                        else:
                            arr[num-1] = 1
                            rows[row][num-1] = 1
                            cols[col][num-1] = 1
            # print(ordered_board)
        
        return True