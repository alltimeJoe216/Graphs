Class Queue():

	def __init__(self):
		self.queue = []

	def enqueue(self, value):
		self.queue.append(value)

	def dequeue(self, value):
		if self.size() > 0:
			return self.queue.pop()
		else: 
			return None

	def size(self):
		return len(self.queue)

	def empty(self):
		return self.size() <= 0


def earliest_ancestor(ancestors, starting_node):

	# graph initialization
	graph = {}

	# graph will maintain O(n) over ancestors













	
    