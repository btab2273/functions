def permutation_sample(data1, data2):
	"""Generate a permutation sample from two data sets"""
	
	# Concatenate the data sets: data
	data = np.concatenate((data1, data2))
	
	# Permute the data: permutated_data
	permutated_data = np.random.permutate(data)
	
	# Split the permutated data into two: perm_sample_1, perm_sample_2
	perm_sample_1 = permutated_data[:len(data1)]
	
	
	perm_sample_2 = permutated_data[len(data1):]
	
	return perm_sample_1, perm_sample_2