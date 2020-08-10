



class BoardSolver:

    def __init__(self, board):
        """
        initializes the board solver class with a given board
        """

        self.board = board

    
    def __repr__(self):
        """
        represents the board as a string when printed
        """
        return_str = ''

        for i in range(1, 10):
            for j in range(1, 10):
                return_str += (str(self.board[i-1][j-1]) + ' ')

                if j%3==0 and j != 9:
                    return_str += '| '
            
            return_str += '\n'

            if i%3==0 and i != 9:
                return_str += '---------------------\n'

        return return_str

    __str__ = __repr__

    def TestColumn(self, y, value):
        """
        given an y location on the board
        tests to see if the value is already in the column
        """
        if value in [row[y] for row in self.board]:
            return False
        return True 

    def TestRow(self, x, value):
        """
        given an x location on the board
        tests to see if the value is already in the row
        """

        if value in self.board[x]:
            return False
        return True

    def TestSquare(self, x, y, value):
        """
        finds the square that the x, y is in 
        tests to see if the value is already in the square
        """
        sqare_x = 0
        square_y = 0
        num_list = []

        if x > 2 and x < 6:
            sqare_x = 3
        elif x > 5:
            sqare_x = 6

        if y > 2 and y < 6:
            square_y = 3
        elif y > 5:
            square_y = 6
        
        for i in range(3):
            for j in range(3):
                num_list.append(self.board[i + sqare_x][j + square_y])

        if value in num_list:
            return False
        return True

    def GetNextOpenSpace(self, x, y):

        newX = x
        newY = y

        if newX == 8 and newY == 8:
            return -1, -1

        while 1:
            if newY == 8:
                newY = 0
                newX += 1
            else:
                newY += 1

            if self.board[newX][newY] == 0:
                return newX, newY

    def SolveGame(self, x, y):

        if x == -1 and y == -1:
            return True

        for i in range(1, 10):
            if self.TestColumn(y, i) and self.TestRow(x, i) and self.TestSquare(x, y, i):
                self.board[x][y] = i
                newX, newY = self.GetNextOpenSpace(x, y)
                if self.SolveGame(newX, newY):
                    return True

                self.board[x][y] = 0

        return False

def main():

    newBoard = BoardSolver([[0, 0, 7, 3, 0, 0, 0, 0, 6], 
                            [0, 0, 2, 0, 0, 6, 3, 0, 7], 
                            [6, 4, 0, 0, 0, 7, 0, 8, 0], 
                            [2, 1, 6, 7, 0, 0, 0, 5, 0], 
                            [0, 7, 0, 1, 0, 5, 0, 9, 0], 
                            [0, 5, 0, 0, 0, 4, 1, 7, 2], 
                            [0, 3, 0, 4, 0, 0, 0, 6, 5], 
                            [7, 0, 4, 5, 0, 0, 9, 0, 0], 
                            [9, 0, 0, 0, 0, 3, 2, 0, 0]])
    
    print(newBoard)

    print('\n\n\n')

    startX, startY = newBoard.GetNextOpenSpace(0, -1)

    newBoard.SolveGame(startX, startY)

    print(newBoard)


if __name__ == "__main__":
    main()
