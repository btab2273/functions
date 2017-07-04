def boostrap_replicate_1d(data, func):
	""" Generate bootstrap replicate of 1D data """
	bs_sample = np.random.choice(data, len(data))
	return func(bs_sample)
	
	