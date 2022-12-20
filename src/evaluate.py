import chess

INITIAL_SIDE_VALUE = 8 * 1 + 1 * 9 + 4 * 3 + 2 * 5
MAX_SIDE_VALUE = 9 * 9 + 4 * 3 + 2 * 5

LOSE_VALUE = 1
DRAW_VALUE = 2 + MAX_SIDE_VALUE
WIN_VALUE = 2 + 2 * MAX_SIDE_VALUE + 1

BELOW_VAL_RANGE = 0
ABOVE_VAL_RANGE = WIN_VALUE + 1

PIECE_VALUES = {
	chess.PAWN: 1,
	chess.KNIGHT: 3,
	chess.BISHOP: 3,
	chess.ROOK: 5,
	chess.QUEEN: 9
}

# AntiBoard -> Color -> int
def evaluate(board, side):
	# returns an int in range(1,101)

	# CASE: Game is over
	outcome = board.outcome()
	is_draw = False
	if outcome is not None:
		winner = outcome.winner

		if winner == None:
			is_draw = True
		elif winner == side:
			return WIN_VALUE
		else:
			return LOSE_VALUE

	# CASE: Heuristic
	player_value = 0
	opponent_value = 0
	for piece, value in PIECE_VALUES.items():
		player_value += board.pieces_count(piece, side) * value
		opponent_value += board.pieces_count(piece, not side) * value

	# CASE: there's less pieces on the board AND we have a draw opportunity
	if is_draw and player_value + opponent_value < INITIAL_SIDE_VALUE:
		return DRAW_VALUE

	return 2 + MAX_SIDE_VALUE + player_value - opponent_value

