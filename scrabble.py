from random import shuffle

letterScores = { "A": 1,
                 "B": 3,
                 "C": 3,
                 "D": 2,
                 "E": 1,
                 "F": 4,
                 "G": 2,
                 "H": 4,
                 "I": 1,
                 "J": 1,
                 "K": 5,
                 "L": 1,
                 "M": 3,
                 "N": 1,
                 "O": 1,
                 "P": 3,
                 "Q": 10,
                 "R": 1,
                 "S": 1,
                 "T": 1,
                 "U": 1,
                 "V": 4,
                 "W": 4,
                 "X": 8,
                 "Y": 4,
                 "Z": 10,
                 "#": 0}

class Board:
    def __init__(self):
        self.board = [["   " for i in range(15)] for j in range(15)]
        for i in range(0, 15):
            for j in range(0, 15):
                self.board[i][j] = "..."
        self.BonusSquares()
        self.board[7][7] = ".*."

    def GetBoard(self):
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.board)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def BonusSquares(self):
        TRIPLEWORDSQ = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DOUBLEWORDSQ = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        TRIPLELETTERSQ = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        DOUBLELETTERSQ = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

        for coordinate in TRIPLEWORDSQ:
            self.board[coordinate[0]][coordinate[1]] = "TWS"
        for coordinate in TRIPLELETTERSQ:
            self.board[coordinate[0]][coordinate[1]] = "TLS"
        for coordinate in DOUBLEWORDSQ:
            self.board[coordinate[0]][coordinate[1]] = "DWS"
        for coordinate in DOUBLELETTERSQ:
            self.board[coordinate[0]][coordinate[1]] = "DLS"

    def Update(self, word, row, col, dir):
        row = int(row)
        col = int(col)
        wordLen = len(word)
        if dir == "down":
            for i in range(row, row + wordLen):
                print(word[i-row])
                self.board[i][col] = "." + word[i-row] + "."
        if dir == "right":
            for i in range(col, col + wordLen):
                self.board[row][i] = "." + word[i-col] + "."


class Pool:
    def __init__(self):
        self.pool = []
        self.Initialize()

    def Initialize(self):
        self.AddToPool(Tile("A", letterScores), 9)
        self.AddToPool(Tile("B", letterScores), 2)
        self.AddToPool(Tile("C", letterScores), 2)
        self.AddToPool(Tile("D", letterScores), 4)
        self.AddToPool(Tile("E", letterScores), 12)
        self.AddToPool(Tile("F", letterScores), 2)
        self.AddToPool(Tile("G", letterScores), 3)
        self.AddToPool(Tile("H", letterScores), 2)
        self.AddToPool(Tile("I", letterScores), 9)
        self.AddToPool(Tile("J", letterScores), 9)
        self.AddToPool(Tile("K", letterScores), 1)
        self.AddToPool(Tile("L", letterScores), 4)
        self.AddToPool(Tile("M", letterScores), 2)
        self.AddToPool(Tile("N", letterScores), 6)
        self.AddToPool(Tile("O", letterScores), 8)
        self.AddToPool(Tile("P", letterScores), 2)
        self.AddToPool(Tile("Q", letterScores), 1)
        self.AddToPool(Tile("R", letterScores), 6)
        self.AddToPool(Tile("S", letterScores), 4)
        self.AddToPool(Tile("T", letterScores), 6)
        self.AddToPool(Tile("U", letterScores), 4)
        self.AddToPool(Tile("V", letterScores), 2)
        self.AddToPool(Tile("W", letterScores), 2)
        self.AddToPool(Tile("X", letterScores), 1)
        self.AddToPool(Tile("Y", letterScores), 2)
        self.AddToPool(Tile("Z", letterScores), 1)
        self.AddToPool(Tile("#", letterScores), 2)
        shuffle(self.pool)

    def AddToPool(self, tile, quantity):
        for i in range(quantity):
            self.pool.append(tile)

    def TakeFromPool(self):
        #Removes a tile from the bag and returns it to the user. This is used for replenishing the rack.
        return self.pool.pop()


class Tile:
    def __init__(self, letter, letter_vals):
        self.letter = letter
        self.score = letter_vals[self.letter]

    def GetLetter(self):
        return self.letter

    def GetScore(self):
        return self.score

class Rack:
    def __init__(self, pool):
        self.rack = []
        self.pool = pool
        self.Initialize()

    def Initialize(self):
        for i in range(7):
            self.AddToRack()

    def AddToRack(self):
        self.rack.append(self.pool.TakeFromPool())

    def ShowRack(self):
        for i in self.rack:
            print(i.GetLetter(), flush = True, end = ", ")
        print("\n")

    def RackWordCompare(self, word):
        L = len(word)
        l = 0
        for i in word:
            for j in self.rack:
                if i == j.GetLetter():
                    l = l+1
                if l == L:
                    return True

class Player:
    def __init__(self, pool):
        self.rack = Rack(pool)
        self.Begin()

    def Begin(self):
        P1Name = input("Enter Name \nPlayer1: ")

    def Turn(self):
        self.rack.ShowRack()
        word = input("write a word: ")
        row = input("choose a row: ")
        col = input("choose a Column: ")
        dir = input("choose a direction (down or right): ")
        return word, row, col, dir

def GameLoop():
    # Begin()
    pool = Pool()
    p1 = Player(pool)
    board = Board()
    print(board.GetBoard())
    word, row, col, dir = p1.Turn()
    board.Update(word, row, col, dir)
    print(board.GetBoard())


GameLoop()
