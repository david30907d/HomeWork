import scipy, pandas, numpy
import numpy as np
from collections import Counter
from sklearn.preprocessing import Normalizer, MinMaxScaler
from sklearn.cross_validation import KFold
from sklearn import neighbors
import matplotlib.pyplot as plt

class KNN(object):
	"""docstring for KNN"""
	def __init__(self, nor='nor', fold=2):
		self.fold = fold
		dataframe = pandas.read_csv(open('wine.data'))
		array = dataframe.values
		# separate array into input and output components
		self.X = array[:,1:]
		self.Y = array[:,0]
		# normalizer can turn length of vector into 1.
		if nor == 'nor':
			scaler = Normalizer().fit(self.X)
		else:
			scaler = MinMaxScaler().fit(self.X)

		self.data = scaler.transform(self.X)
		numpy.set_printoptions(precision=3)
		# print(self.data[0:5,:])

	def classify(self, testset_vec, trainset_vec, trainset_class, k=5):
		"""
		Do classification job
		:param input_vec
		:param trainset_vec
		:param trainset_class
		:param k: how many neighbors
		:return: class it predict, it's an array
		"""
		result = []
		for input_vec in testset_vec:
			vec_distance = []
			for v, c in zip(trainset_vec, trainset_class):
				euclidean_distance = np.linalg.norm(np.array(input_vec)-np.array(v))
				vec_distance.append((c, euclidean_distance))
			sorted_distance = sorted(vec_distance, key=lambda x:x[1])
			top_nearest = [c for c, distance in sorted_distance[:k]]
			result.append(Counter(top_nearest).most_common(1)[0][0])
		return result

	def evaluate(self, k=5):
		itertimes = 20
		accuracy = 0
		sk_acc = 0
		clf = neighbors.KNeighborsClassifier()
		for _ in range(itertimes):
			kf = KFold(len(self.data), n_folds=self.fold, shuffle=True)
			for train_index, test_index in kf:
				X_train, X_test = self.X[train_index], self.X[test_index]
				Y_train, Y_test = self.Y[train_index], self.Y[test_index]
				predict = self.classify(X_test, X_train, Y_train, k)
				accuracy += len([1 for i,j in zip(predict, Y_test) if i==j]) / len(Y_test)

				# cmp with sklearn performance
				clf.fit(X_train, Y_train)
				sk_acc += clf.score(X_test, Y_test)
		print('k: {}, my knn:{}, sklearn\'s knn:{}'.format(k, accuracy / self.fold / itertimes, sk_acc/self.fold/itertimes))
		return (accuracy / self.fold / itertimes, sk_acc/self.fold/itertimes)

	def visualize(self, k):
		mylist, klist = [], []
		for i in range(1, k+1):
			my_acc, k_acc = self.evaluate(k=i)
			mylist.append(my_acc)
			klist.append(k_acc)
		# axes = plt.gca()
		# axes.set_ylim([0.419,0.44])
		plt.plot(range(1, k+1), mylist, label='my knn')
		plt.plot(range(1, k+1), klist, label='sklearn')
		plt.title('Train History')
		plt.ylabel('acc')
		plt.xlabel('k neighbors')
		plt.legend(loc='best')
		plt.show()

if __name__ == '__main__':
	# normalize
	k = KNN()
	k.evaluate()
	k.visualize(10)


	# min-Max
	k = KNN(nor='min-max')
	k.evaluate()
	k.visualize(10)