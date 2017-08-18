# Define path_exists()
def path_exists(G, node1, node2):
	"""
	Breadth-first seach algorithim
	This function checks whether a path exists between two nodes( node1, node2) in graph G.
	"""
	visited_nodes = set()

	# Initialize the queue of cells to visit with the first node: queue
	queue = [node1]

	# Iterate over the nodes in the queue
	for node in queue:

		# Get neighbors of the node
		neighbors = G.neighbors(node)

		# Check to see if the destination node is in the set of neighbors
		if node2 in neighbors:
			print('Path exists between nodes {0} and {1}'.format(node1, node2))
			return True
			break
		else:
			# Add neighbors of current node that have not yet been visited
			queue.extend([n for n in neighbors if n not in visited_nodes])



		# Check to see if the final element of the queue has been reached
		if node == queue[-1]:
			print('The path does not exist between nodes {0} and {1}'.format(node1, node2))
			return False


