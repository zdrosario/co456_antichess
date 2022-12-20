import chess
import sys

from antichess import AntiBoard
from pickmove import MovePicker

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
	move_picker = MovePicker()

	while not board.is_game_over():
		if board.turn == side:
			if not move_picker.initialized:
				move_picker.init_with_board(board)

			uci = move_picker.pick_move()

			board.push_uci(uci)
			move_picker.step_down(uci)

			print(uci)
		else:
			uci = input()

			board.push_uci(uci)
			if move_picker.initialized:
				move_picker.step_down(uci)
				move_picker.generate_levels(board)
			# TODO: exception handling?

if __name__ == "__main__":
	main(len(sys.argv), sys.argv)
