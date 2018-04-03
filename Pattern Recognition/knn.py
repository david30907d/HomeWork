import scipy, pandas, numpy
import numpy as np
from collections import Counter
from sklearn.preprocessing import Normalizer
from sklearn.cross_validation import KFold

class KNN(object):
	"""docstring for KNN"""
	def __init__(self, k=5, fold=2):
		self.k = k
		self.fold = fold
		dataframe = pandas.read_csv(open('wine.data'))
		array = dataframe.values
		# separate array into input and output components
		self.X = array[:,1:]
		self.Y = array[:,0]
		# normalizer can turn length of vector into 1.
		scaler = Normalizer().fit(self.X)

		self.data = scaler.transform(self.X)
		numpy.set_printoptions(precision=3)
		# print(self.data[0:5,:])

	def classify(self, testset_vec, trainset_vec, trainset_class):
		"""
		執行kNN分類演算法
		:param input_vec: 輸入向量
		:param trainset_vec: 訓練集合向量
		:param trainset_class: 訓練集合分類
		:return: class
		"""
		# 計算每個訓練集合特徵關鍵字字詞頻率向量和輸入向量的距離
		result = []
		for input_vec in testset_vec:
			vec_distance = dict()
			for v, c in zip(trainset_vec, trainset_class):
				euclidean_distance = np.linalg.norm(np.array(input_vec)-np.array(v))
				vec_distance[euclidean_distance] = c
			result.append(max(Counter([c for distance, c in sorted(vec_distance.items(), key=lambda x:x[0])[:self.k]]).items(), key=lambda x:x[1])[0])
		return result

	def evaluate(self):
		folds, itertimes = 2, 20
		accuracy = 0
		for _ in range(itertimes):
			kf = KFold(len(self.data), n_folds=folds, shuffle=True)
			for train_index, test_index in kf:
				X_train, X_test = self.X[train_index], self.X[test_index]
				y_train, y_test = self.Y[train_index], self.Y[test_index]
				predict = self.classify(X_test, X_train, y_train)
				accuracy += len([1 for i,j in zip(predict, y_test) if i==j]) / len(y_test)
		print(accuracy / folds / itertimes)

if __name__ == '__main__':
	k = KNN()
	k.evaluate()