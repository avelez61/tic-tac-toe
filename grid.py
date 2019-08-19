class Grid:
    def __init__(self):
        self.EMPTY = '.'
        self.CHAR_X = 'X'
        self.CHAR_O = 'O' 
        self.grid = []
        self.turn = 'X'
        self.playing = True

        #Grid initalization
        for i in range(3):
            self.grid.append([])
            for j in range(3):
                self.grid[i].append(self.EMPTY)

    # OBSOLETE FUNCTION
    def print_grid(self): 
        for i in range(3):
            if i != 0:
                print()
            for j in range(3):
                print(self.grid[i][j], end = ' ')
        print()

    def get_move(self, mouse_pos):
        move = []
        move.append(int(mouse_pos[1] / 64)) # WINDOW DEPENDANT
        move.append(int(mouse_pos[0] / 64)) # WINDOW DEPENDANT
        return move

    def space_empty(self, move):
        return self.grid[move[0]][move[1]] == self.EMPTY

    def make_move(self, move):
        self.grid[move[0]][move[1]] = self.turn

    # OBSOLETE FUNCTION
    def print_end(self, tie):
        if not tie:
            print(self.turn, ' Wins!')
        else:
            print('Tie!')
        self.print_grid()

    #SIZE DEPENDANT FUNCTION
    def check_end(self, row, col):
        if all(self.grid[row][i] == self.turn for i in range(3)):
            return True
        elif all(self.grid[i][col] == self.turn for i in range(3)):
            return True
        elif all(self.grid[i][i] == self.turn for i in range(3)):
            return True
        elif all(self.grid[i][2 - i] == self.turn for i in range(3)):
            return True
        # May be able to below trick for above checks
        elif not any(self.EMPTY in row for row in self.grid):
            return True
        else:
            return False

    def change_turn(self):
        if self.turn == self.CHAR_X:
            self.turn = self.CHAR_O
        elif self.turn == self.CHAR_O:
            self.turn = self.CHAR_X

    def reset(self):
        self.playing = True
        self.turn = self.CHAR_X
        for i in range(3):
            for j in range(3):
                self.grid[i][j] = self.EMPTY
