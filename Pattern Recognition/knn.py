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
		self.nor = nor
		# normalizer can turn length of vector into 1.
		if self.nor == 'nor':
			scaler = Normalizer().fit(self.X)
		else:
			scaler = MinMaxScaler().fit(self.X)

		self.X = scaler.transform(self.X)
		numpy.set_printoptions(precision=3)
		# print(self.X[0:5,:])

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
		train_accuracy = 0
		test_accuracy = 0
		sk_test_acc = 0
		clf = neighbors.KNeighborsClassifier()
		for _ in range(itertimes):
			kf = KFold(len(self.X), n_folds=self.fold, shuffle=True)
			for train_index, test_index in kf:
				X_train, X_test = self.X[train_index], self.X[test_index]
				Y_train, Y_test = self.Y[train_index], self.Y[test_index]

				# use traing set
				predict = self.classify(X_train, X_train, Y_train, k)
				train_accuracy += len([1 for i,j in zip(predict, Y_train) if i==j]) / len(Y_test) / self.fold / itertimes			

				# use testing set
				predict = self.classify(X_test, X_train, Y_train, k)
				test_accuracy += len([1 for i,j in zip(predict, Y_test) if i==j]) / len(Y_test) / self.fold / itertimes

				# cmp with sklearn performance
				clf.fit(X_train, Y_train)
				sk_test_acc += clf.score(X_test, Y_test) / self.fold / itertimes
		print('k: {}, my knn using traingSet:{} my knn:{}, sklearn\'s knn:{}'.format(k, train_accuracy, test_accuracy, sk_test_acc))
		return (train_accuracy, test_accuracy, sk_test_acc)

	def visualize(self, k):
		myTrainList, mylist, klist = [], [], []
		for i in range(1, k+1):
			myTrain_acc, my_acc, k_acc = self.evaluate(k=i)
			myTrainList.append(myTrain_acc)
			mylist.append(my_acc)
			klist.append(k_acc)
		# axes = plt.gca()
		# axes.set_ylim([0.419,0.44])
		plt.plot(range(1, k+1), myTrainList, label='my knn using Training Set')
		plt.plot(range(1, k+1), mylist, label='my knn')
		plt.plot(range(1, k+1), klist, label='sklearn')
		plt.title('Train History')
		plt.ylabel('acc')
		plt.xlabel('k neighbors')
		plt.legend(loc='best')
		plt.savefig('{}.png'.format(self.nor))
		plt.show()

if __name__ == '__main__':
	# normalize
	k = KNN(nor='normalization')
	k.evaluate()
	k.visualize(10)


	# min-Max
	k = KNN(nor='min-max')
	k.evaluate()
	k.visualize(10)