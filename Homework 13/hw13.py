'''
Created on 12/5/2022 
@author: Anthony Curcio-Petraccoro 
Pledge: I pledge my honor that I have abided by the Stevens Honor System. 
CS115 - HW 13 (BONUS) 
'''

class Board:
    def __init__(self, width = 7, height = 6):
        '''Properly instantiates all variables.'''
        self.width = width
        self.height = height
        self.data = [[" "]*width for row in range(height)]

    def __str__(self):
        '''Creates the board.'''
        num = 0
        board = ""
        L = []
        for row in range(0, self.height):
            board += "|"
            for col in range(0, self.width):
                board += self.data[row][col] + "|"
            board += "\n"
        board += (2 * self.width + 1) * "-"
        board += "\n "
        for i in range(self.width):
            if i == 10:
                num = 0
                board += str(num) + " "
                num += 1
            else:
                board += str(num) + " "
                num += 1
        board += "\n"
        return board

    def allowsMove(self, col):
        '''Checks to see if a chip is already in this column.'''
        if col > self.width and col < 0:
            return False
        for i in range(self.width - 1):
            if self.data[i][col] == " ":
                return True 
        return False

    def addMove(self, col, ox):
        '''Adds a chip in the column if there isn't already one there.'''
        if self.allowsMove(col) == True:
            if self.data[self.height - 1][col] == " ":
                self.data[self.height - 1][col] = str(ox)
            else:
                for i in range(self.width - 2):
                    if self.data[i][col] == " ":
                        if self.data[i + 1][col] != " ":
                            self.data[i][col] = str(ox)

    def delMove(self, col):
        '''Deletes the top row in a given column.'''
        for i in range(self.width - 2):
            if self.data[i][col] == " ":
                if self.data[i + 1][col] != " ":
                    self.data[i + 1][col] = " "
                
    def setBoard(self, moveString):
        '''takes in a string of columns and places alternating checkers in those columns, starting with "X". For example, call b.setBoard('012345') to see "X"s and "O"s alternate on the bottom row, or b.setBoard('000000') to see them alternate in the left column. MoveString must be a string of integers'''  
        nextCh = "X"
        for colString in moveString: 
            col = int(colString) 
            if 0 <= col <= self.width: 
                self.addMove(col, nextCh) 
            if nextCh == "X":
                nextCh = "O"
            else:
                nextCh = "X"

    def winsFor(self, ox):
        '''Checks all instances of a win. Returns True if a player has one, returns False otherwise.'''
        for a in range(self.height):
            for b in range(self.width - 3):
                if self.data[a][b] == ox:
                   if self.data[a][b + 1] == ox:
                       if self.data[a][b + 2]  == ox:
                           if self.data[a][b + 3] == ox:
                                return True
        for c in range(self.height - 3):
            for d in range(self.width):
                if self.data[c][d] == ox:
                    if self.data[c + 1][d] == ox:
                        if self.data[c + 2][d]  == ox:
                            if self.data[c + 3][d] == ox:
                                return True
        for e in range(self.width - 3):
            for f in range(self.height - 3):
                if self.data[e][f] == ox:
                   if self.data[e + 1][f + 1] == ox:
                        if self.data[e + 2][f + 2]  == ox: 
                            if self.data[e + 3][f + 3] == ox:
                                return True
        for g in range(self.height):
            for h in range(self.width - 3):
                if self.data[g][h] == ox:
                    if self.data[g - 1][h + 1] == ox:
                        if self.data[g - 2][h + 2]  == ox:
                            if self.data[g - 3][h + 3] == ox:
                                return True
        else: 
            return False
    
    def hostGame(self):
        '''Creates a user input section.''' 
        print("Welcome to Connect Four!")
        player = "X"
        choice = -1
        print(self + "\n")
        while True:
            i = 0
            while i == 0:
                if player == "X":
                    try:
                        choice = int(input("X's choice: "))
                        i = 1
                    except ValueError:
                        i = 0
                else:
                    try:
                        choice = int(input("O's choice: "))
                        i = 1
                    except ValueError:
                        correctInput = 0
                if i == 1 and self.allowsMove(choice):
                    i = 1
                else:
                    print("Please input a number.")
                    i = 0
            if player == "X":
                self.addMove(choice, "X")
                player = "O"
            else:
                self.addMove(choice, "O")
                player = "X"
            print("\n")
            if self.winsFor("X"):
                print("\n")
                print("X wins -- Congratulations!")
                print("\n")
                print(self)
                break
            elif self.winsFor("X"):
                print("\n")
                print("O wins -- Congratulations!")
                print("\n")
                print(self)
                break
            print(self)
            print("\n")
                
if __name__ == '__main__':
    '''Runs the interface and prompts the user with a reponse.'''
    b = Board()
    b.hostGame()
