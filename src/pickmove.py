from evaluate import ABOVE_VAL_RANGE, BELOW_VAL_RANGE, evaluate
from minimaxnode import MAX_NODE, MIN_NODE, MinimaxNode

INITIAL_DEPTH = 3
MAX_DEPTH = 3

node_count = 1

# AntiBoard -> MinimaxNode -> int -> MinimaxNode
def add_children(board, node, depth = 1):
	if (depth == 0):
		return node

	legal_moves = board.generate_legal_moves()
	for move in legal_moves:
		uci = move.uci()

		child_node = node.get_child(uci)
		if child_node is None:
			child_node = MinimaxNode(not node.type)
			node.add_child(uci, child_node)

		board.push_uci(uci)
		add_children(board, child_node, depth = depth - 1)
		board.pop()

	return node

# AntiBoard -> Color -> MinimaxNode -> int
def fill_values(board, side, node):
	if len(node.children) == 0:
		value = evaluate(board, side)
		node.set_value(value)

		return value

	cur_val = BELOW_VAL_RANGE if node.type == MAX_NODE else ABOVE_VAL_RANGE
	cur_uci = ""
	for uci, child in node.children.items():
		board.push_uci(uci)
		child_val = fill_values(board, side, child)
		board.pop()

		do_update = node.type == MAX_NODE and child_val > cur_val \
			or node.type == MIN_NODE and child_val < cur_val
		
		if do_update:
			cur_val = child_val
			cur_uci = uci

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
		self.generate_levels(board, depth = INITIAL_DEPTH)

		self.initialized = True

	# MovePicker -> str -> MinimaxNode
	def step_down(self, uci):
		self.root = self.root.remove_child(uci)
		return self.root

	# MovePicker -> str
	def pick_move(self):
		return self.root.get_move()

	# MovePicker -> None
	def generate_levels(self, board, depth = MAX_DEPTH):
		add_children(board, self.root, depth = depth)
		fill_values(board, self.side, self.root)
