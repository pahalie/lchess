import chess

class State(object):
	def __init__(self):
		self.board = chess.Board()

	def value(self):
		return 1

	def edges(self):
		return list(self.board.legal_moves)

if __name__ == '__main__':
	s = State()
	legal_moves = s.edges()
	import pdb;pdb.set_trace()
