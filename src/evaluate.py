import chess

MAX_SIDE_VALUE = 9 * 9 + 4 * 3 + 2 * 5

WIN_VALUE = 1
DRAW_VALUE = 2 + MAX_SIDE_VALUE
LOSE_VALUE = DRAW_VALUE + MAX_SIDE_VALUE + 1

BELOW_VAL_RANGE = 0
ABOVE_VAL_RANGE = LOSE_VALUE + 1

# AntiBoard -> Color -> int
def evaluate(board, side):
	# returns an int in range(1,101)

	# CASE: Game is over
	outcome = board.outcome()
	if outcome is not None:
		winner = outcome.winner

		if winner == None:
			return DRAW_VALUE
		elif winner == side:
			return WIN_VALUE
		else:
			return LOSE_VALUE

	# CASE: Heuristic
	piece_values = {
		chess.PAWN: 1,
		chess.KNIGHT: 3,
		chess.BISHOP: 3,
		chess.ROOK: 5,
		chess.QUEEN: 9
	}

	player_value = 0
	opponent_value = 0
	for piece, value in piece_values.items():
		player_value += board.pieces_count(piece, side) * value
		opponent_value += board.pieces_count(piece, not side) * value

	return 3 + MAX_SIDE_VALUE + player_value - opponent_value
