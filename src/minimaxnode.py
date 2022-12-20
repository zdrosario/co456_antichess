from evaluate import ABOVE_VAL_RANGE, BELOW_VAL_RANGE

NODE_TYPES = [MAX_NODE, MIN_NODE] = [True, False]

class MinimaxNode:
	# MinimaxNode -> NodeType -> Ozptional[MinimaxNode] -> None
	def __init__(self, type):
		self.type = type
		self.value = BELOW_VAL_RANGE if type == MAX_NODE else ABOVE_VAL_RANGE
		self.move = ""
		
		self.parent = None
		self.children = {}
	
	# MinimaxNode -> str -> MinimaxNode -> MinimaxNode
	def add_child(self, uci, child):
		self.children[uci] = child
		child.parent = self
		return child

	# MinimaxNode -> str -> Optional[MinimaxNode]
	def remove_child(self, uci):
		child = self.children.pop(uci)
		if (child != None):
			child.parent = None
		return child

	# MinimaxNode -> str -> Optional[MinimaxNode]
	def get_child(self, uci):
		return self.children.get(uci)

	# MinimaxNode -> int -> int
	def set_value(self, val):
		self.value = val
		return val

	# MinimaxNode -> str -> str
	def set_move(self, uci):
		self.move = uci
		return uci

	# MinimaxNode -> int
	def get_value(self):
		return self.value

	# MinimaxNode -> str
	def get_move(self):
		return self.move
