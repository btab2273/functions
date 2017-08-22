# Write a function that identifies all nodes in a triangle relationship
# with a give node

import networkx as networkx
from itertools import combinations

def nodes_in_triangle(G, n):
	"""
	Returns the nodes in a graph 'G' that are involved in a triangle
	relationship with the node 'n'
	"""
	triangle_nodes = set([n])

	# Iterate over all possible triangle relationship combinations
	for n1, n2 in combinations(G.neighbors(n), 2):

		# Check if n1 and n2 have an edge between them
		if G.has_edge(n1, n2):

			# Add n1 to triangle_nodes
			triangle_nodes.add(n1)

			# Add n2 to triangle_nodes
			triangle_nodes.add(n2)

	return triangle_nodes


# Use the function in a assert statement to check if the number of nodes
# involved in a triangle relationship with node 1 of graph T is equal
# to 35
assert len(nodes_in_triangle(T, 1)) == 35