import os
import chess.pgn
from state import State

for f in os.listdir("data"):
	pgn = open(os.path.join("data", f))

	while 1:
		try:
			game = chess.pgn.read_game(pgn)
		except Exception:
			break
		if game:
			value = {'1-0': 1, '0-1': -1, '1/2-1/2': 0}[game.headers['Result']]
			board = game.board()

			for move in game.mainline_moves():
				board.push(move)

				print(State(board).serialize())
