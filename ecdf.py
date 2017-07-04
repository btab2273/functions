import numpy as np

def ecdf(data):
	""" Compute ECDF for a one-dimensional array of measurments """
	
	# Number of data points: n
	n = len(data)
	
	# x-data for the ecdf: x
	x = np.sort(data)
	
	# y-data for the ecdf: y
	y = np.arange(1, len(x)+1)/n
	
	return x,y