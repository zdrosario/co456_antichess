from evaluate import ABOVE_VAL_RANGE, BELOW_VAL_RANGE, evaluate
from minimaxnode import MAX_NODE, MIN_NODE, MinimaxNode

MAX_DEPTH = 20

# AntiBoard -> Color -> MinimaxNode -> int -> int
def fill_values(board, side, node, depth):
	return ab_fill_values(board, side, node, depth, BELOW_VAL_RANGE, ABOVE_VAL_RANGE)

# AntiBoard -> Color -> MinimaxNode -> int -> int -> int -> int
def ab_fill_values(board, side, node, depth, a, b):
	legal_moves = board.generate_legal_moves()

	if len(legal_moves) == 0 or depth == 0:
		value = evaluate(board, side)
		node.set_value(value)
		return value

	cur_val = BELOW_VAL_RANGE if node.type == MAX_NODE else ABOVE_VAL_RANGE
	cur_uci = ""

	if node.type == MAX_NODE:
		for move in legal_moves:
			uci = move.uci()
			child = node.get_child(uci)
			if child is None:
				child = MinimaxNode(not node.type)
				node.add_child(uci, child)

			board.push(move)
			child_val = ab_fill_values(board, side, child, depth - 1, a, b)
			board.pop()

			if child_val >= b:
				break

			if child_val > cur_val:
				cur_val = child_val
				cur_uci = uci

			a = max(a, cur_val)

	else:
		for move in legal_moves:
			uci = move.uci()
			child = node.get_child(uci)
			if child is None:
				child = MinimaxNode(not node.type)
				node.add_child(uci, child)

			board.push(move)
			child_val = ab_fill_values(board, side, child, depth - 1, a, b)
			board.pop()

			if child_val <= a:
				break

			if child_val < cur_val:
				cur_val = child_val
				cur_uci = uci

			b = min(b, cur_val)

	node.set_value(cur_val)
	node.set_move(cur_uci)
	return cur_val

class MovePicker:
	def __init__(self):
		self.initialized = False

	# MovePicker -> AntiBoard -> None
	def init_with_board(self, board):
		self.side = board.turn

		self.root = MinimaxNode(MAX_NODE)
		self.generate_levels(board)

		self.initialized = True

	# MovePicker -> AntiBoard -> str -> MinimaxNode
	def step_down(self, board, uci):
		new_root = self.root.get_child(uci)
		if new_root == None:
			new_root = MinimaxNode(not self.root.type)
		else:
			self.root.remove_child(uci)

		self.root = new_root
		return self.root

	# MovePicker -> str
	def pick_move(self):
		return self.root.get_move()

	# MovePicker -> None
	def generate_levels(self, board):
		fill_values(board, self.side, self.root, depth = MAX_DEPTH)
