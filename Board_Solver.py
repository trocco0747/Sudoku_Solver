



class BoardSolver:

    def __init__(self, board):
        """
        """

        self.board = board

    
    def __repr__(self):
        """
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


if __name__ == "__main__":
    main()
