import networkx as nx
fromm itertools import combinations

def node_in_open_triangle(G, n):
	"""
	Checks whether pairs of neighbors of node 'n' in graph 'G' are in 
	an 'open triangle' relationship with node 'n'
	"""

	# Iterate over all possible triangle relationship combinations
	for n1, n2 in combinations(G.neighbors(n), 2):

		# Check if n1 and n2 do NOT have an edge between them
		if not G.has_edge(n1, n2):

			node_in_open_triangle = True

			break
	return node_in_open_triangle

# Compute the number of open triangles in T
num_open_triangles = 0

# Iterate over all the nodes in T
for n in T.nodes():

	# Check if the current node is an open triangle
	if node_in_open_triangle(T, n):

		# Increment num_open_triangles
		num_open_triangles+=1
print(num_open_triangles)