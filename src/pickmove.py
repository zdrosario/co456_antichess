# AntiBoard -> Move
def pick_move(board):
	legal_moves = board.generate_legal_moves()
	return legal_moves[0]
