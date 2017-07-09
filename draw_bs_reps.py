def draw_bs_reps(data, func, size=1):
	"""Draw bootstrap replicates."""
	
	# Initialize array of replicates: bs_replicates
	bs_replicates = np.empty(size)
	
	# Generate replicates
	for i in range(size):
		bs_replicates[i] = bootstrap_replicates(data, func)
		
	return bs_replicates