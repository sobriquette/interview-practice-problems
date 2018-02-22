"""
If hasWon is called many times, preprocess all winning boards, 
by converting each board to an int using a base 3 representation.

3^0 * v0 + 3^1 * v1 + 3^2 * v2... 
where v is a 0 if the space is empty, 1 if red, 2 if blue
"""
class Piece(Enum):
	EMPTY = 0
	RED = 1
	BLUE = 2

class WinningBoards:

	def __init__(self):
		self.winning_boards = {}

	def convert_board_to_int(board):
		sum = 0
		for i in range(len(board)):
			for j in range(len(board[i])):
				val = board[i][j].value
				sum = sum * 3 + value

		return sum

	def has_won(board):
		return self.winning_boards[board]

"""
If we know the last move, we only need to check the row, column, and diagonal
that overlaps with this position.
"""
def has_won_row(board, row):
	return board[row][0] == board[row][1] == board[row][2]

def has_won_col(board, col):
	return board[0][col] == board[1][col] == board[2][col]

def has_won_diagonal(board, direction):
	row = 0
	col = 0 if direction == 1 else (len(board) - 1)
	first = board[row][col]

	for i in range(len(board)):
		if board[row][col] != first:
			return False

		row += 1
		col += direction
	return True

def has_won(board, row, col):
	if len(board) != len(board[0]) or board[row][col] == Piece.EMPTY:
		return Piece.EMPTY

	piece = board[row][col]
	if has_won_row(board, row) or has_won_col(board, col):
		return piece

	if row == col and has_won_diagonal(board, 1):
		return piece

	if row == (len(board) - col - 1) and has_won_diagonal(board, -1):
		return piece

	return Piece.EMPTY

"""
Designing for an NxN board
"""
class Check:
	def __init__(self, row, col, row_increment, col_increment):
		self.row = row
		self.col = col
		self.row_increment = row_increment
		self.col_increment = col_increment

	def increment(self):
		self.row += self.row_increment
		self.col += self.col_increment

	def is_within_bounds(size):
		return self.row >= 0 and self.col >= 0 and \
				self.row < size and self.column < size

def has_won(board):
	if len(board) != len(board[0]):
		return Piece.EMPTY

	size = len(board)
	instructions = []
	for i in range(size):
		instructions.append(Check(0, i, 1, 0))
		instructions.append(Check(i, 0, 0, 1))

	instructions.append(Check(0, 0, 1, 1))
	instructions.append(Check(0, size - 1, 1, -1))

	for instr in instructions:
		winner = is_a_win(board, instr)
		if winner != Piece.EMPTY:
			return winner

	return Piece.EMPTY

def is_a_win(board, instr):
	first = board[instr.row][instr.col]

	while instr.is_within_bounds(len(board)):
		if board[instr.row][instr.col] != first:
			return Piece.EMPTY
		instr.increment()

	return first

