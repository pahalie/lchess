import os
import chess.pgn
from state import State

def get_dataset():
	X, Y = [], []
	gn = 0
	for f in os.listdir("data"):
		pgn = open(os.path.join("data", f))

		while 1:
			gn += 1
			try:
				game = chess.pgn.read_game(pgn)
			except Exception:
				break
			if game:
				print(f"parsing game {gn}, got {len(X)} examples")
				value = {'1-0': 1, '0-1': -1, '1/2-1/2': 0}[game.headers['Result']]
				board = game.board()

				for move in game.mainline_moves():
					board.push(move)
					ser = State(board).serialize()[:,:,0]
					X.append(ser)
					Y.append(value)
			else:
				break
					#print()


if __name__ == "__main__":
	get_dataset()