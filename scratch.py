import chess.pgn

pgn = open("twic1324.pgn")
first_game = chess.pgn.read_game(pgn)
second_game = chess.pgn.read_game(pgn)

board = first_game.board()
for move in first_game.mainline_moves():
	board.push(move)

print(board)

board = second_game.board()
for move in second_game.mainline_moves():
        board.push(move)

pgn = open('twic1324.pgn')
games = []
game = 1

while game:
        game = chess.pgn.read_game(pgn)
        games.append(game)

games = [x for x in games if x]
board = games[0].board()
for move in games[0].mainline_moves():
        board.push(move)

import pdb;pdb.set_trace()
print(board)
