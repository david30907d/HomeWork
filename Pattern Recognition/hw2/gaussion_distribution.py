#!/usr/bin/env python

import numpy as np
import math, json
import matplotlib.pyplot as plt
from itertools import chain

def get_gaussian_random():
	m = 0
	while m == 0:
		m = round(np.random.random() * 100)
	numbers = np.random.random(int(m))
	summation = float(np.sum(numbers))
	gaussian = (summation - m/2) / math.sqrt(m/12.0)
	return gaussian

# get_gaussian_random()

def generate_known_gaussian(dimensions, count):
	ret = []
	for i in range(count):
		current_vector = []
		for j in range(dimensions):
			g = get_gaussian_random()
			current_vector.append(g)
		ret.append(current_vector)
	return ret

# generate_known_gaussian(2)

def stationary_random_process(dimension, p):
	stationary = np.zeros((dimension, dimension))
	np.fill_diagonal(stationary, 1)
	max_len = len(stationary)
	p1, p2 = 1, 1
	for axis in range(len(stationary)):
		another_axis = 0
		axis_backup = axis
		while axis < max_len and another_axis < max_len:
			stationary[axis, another_axis] = p1
			axis += 1
			another_axis += 1
		p1 *= p
		another_axis = 0
		axis = axis_backup
		while another_axis < max_len and axis < max_len:
			stationary[another_axis, axis] = p2
			another_axis += 1
			axis += 1
		p2 *= p
	return stationary

# stationary_random_process(5)

def main(dimension, count, p):
	known = generate_known_gaussian(dimension, count)
	target_cov  = np.matrix(stationary_random_process(dimension, p))
	eigenvalues, eigenvectors = np.linalg.eig(target_cov)
	# 簡單的證明eigenvalue和eigenvector沒算錯
	# print("簡單的證明eigenvalue和eigenvector沒算錯", np.dot(target_cov, eigenvectors) == np.multiply(eigenvalues, eigenvectors))
	l = np.matrix(np.diag(np.sqrt(eigenvalues)))
	Q = np.matrix(eigenvectors) * l
	x1_tweaked = []
	x2_tweaked = []
	tweaked_all = []
	for original in known:
		original = np.matrix(original).T
		tweaked = Q * original
		x1_tweaked.append(tweaked[0])
		x2_tweaked.append(tweaked[1])
		tweaked_all.append(tweaked)

	plt.scatter(x1_tweaked, x2_tweaked)
	plt.show()
	json.dump([list(chain(*i.tolist())) + [p] for i in tweaked_all], open(str(p)+'.json', 'w'))

if __name__ == "__main__":
	main(20, 100, 0.9)
	main(20, 100, 0.5)