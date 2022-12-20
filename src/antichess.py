import chess

class AntiBoard:
	def __init__(self):
		self.board = chess.Board()

	# AntiBoard -> Iterator[Move]
	def generate_legal_moves(self):
		chess_moves = self.board.legal_moves
		capturing_moves = []
		all_moves = []

		for move in chess_moves:
			if self.board.is_capture(move):
				capturing_moves.append(move)
			all_moves.append(move)

		if len(capturing_moves) > 0:
			return capturing_moves
		return all_moves

	# AntiBoard -> Move -> bool
	def is_legal(self, move):
		if not self.board.is_legal(move):
			return False

		return self.board.is_capture(move) or not self.has_captures()

	# AntiBoard -> bool
	def has_captures(self):
		chess_moves = self.board.legal_moves
		for move in chess_moves:
			if self.board.is_capture(move):
				return True
		return False

	# AntiBoard -> Move -> Move
	def push(self, move):
		if self.is_legal(move):
			self.board.push(move)
			return move
		raise ValueError(f"no matching legal move for {move.uci()}")

	# AntiBoard -> str -> Move
	def push_uci(self, uci):
		move = self.board.parse_uci(uci)
		self.push(move)
	
	# AntiBoard -> Move
	def pop(self):
		return self.board.pop()

	# Color
	@property
	def turn(self):
		return self.board.turn

	# AntiBoard -> bool
	def is_check(self):
		return self.board.is_check()

	# AntiBoard -> bool
	def is_game_over(self, claim_draw = True):
		return self.board.is_game_over(claim_draw = claim_draw)

	# AntiBoard -> bool -> Outcome
	def outcome(self, claim_draw = True):
		return self.board.outcome(claim_draw = claim_draw)

	# AntiBoard -> PieceType -> Color -> int
	def pieces_count(self, piece_type, side):
		return len(self.board.pieces(piece_type, side))