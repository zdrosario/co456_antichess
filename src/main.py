import chess
import sys

from antichess import AntiBoard
from pickmove import pick_move

def usage(prog):
	print(f"Usage: {prog} side", file=sys.stderr)
	exit(1)

def main(argc, argv):
	if (argc != 2):
		usage(argv[0])

	side_str = argv[1]
	if (side_str != "white" and side_str != "black"):
		usage(argv[0])
	side = chess.WHITE if side_str == "white" else chess.BLACK

	board = AntiBoard()

	while not board.is_game_over():
		if board.turn == side:
			move = pick_move(board)
			board.push(move)
			print(move)
		else:
			uci = input()
			board.push_uci(uci)
			# TODO: exception handling

if __name__ == "__main__":
	main(len(sys.argv), sys.argv)
