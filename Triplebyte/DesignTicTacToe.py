class TicTacToe:
    def __init__(self, n):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = []
        self.cols = []
        self.diags = [0, 0]
        for row in range(n):

            self.rows.append(0)
            self.cols.append(0)

    def move(self, row, col, player):
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col:
                self.diags[0] += 1
            elif (row + col) == self.n - 1:
                self.diags[1] += 1

            if self.rows[row] == self.n or self.cols[col] == self.n \
                or self.diags[0] == self.n or self.diags[1] == self.n:
                return player
        else:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if row == col:
                self.diags[0] -= 1
            if (row + col) == self.n - 1:
                self.diags[1] -= 1

            if self.rows[row] == -self.n or self.cols[col] == -self.n \
                or self.diags[0] == -self.n or self.diags[1] == -self.n:
                return player

        return 0

#Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
print(obj.move(1,1,2))
print(obj.move(0,2,2))
print(obj.move(2,0,2))
# print(obj.move(0,1,2))
# print(obj.move(1,1,1))












