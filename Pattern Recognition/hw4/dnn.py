from sklearn.preprocessing import Normalizer, MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas
import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam

class DNN(object):
	"""docstring for KNN"""
	def __init__(self, nor='nor'):
		dataframe = pandas.read_csv(open('../wine.data'))
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
		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, test_size=0.5, random_state=42)
		# one hot encode
		self.y_train, self.y_test = to_categorical(np.array(self.y_train))[:,1:], to_categorical(np.array(self.y_test))[:,1:]

	def useTf(self):
		pass

	def useKaras(self):
		model = Sequential()
		model.add(Dense(512, input_shape=(13,), activation='relu'))
		model.add(Dropout(0.5))
		model.add(Dense(512, activation='relu'))
		model.add(Dropout(0.5))
		model.add(Dense(512, activation='relu'))
		model.add(Dropout(0.5))
		model.add(Dense(3, activation='softmax'))
		model.summary()
		model.compile(loss='categorical_crossentropy',
		              optimizer=Adam(),
		              metrics=['accuracy'])
		history = model.fit(self.X_train, self.y_train,
		                    batch_size=4, nb_epoch=1000,
		                    verbose=1, validation_data=(self.X_test, self.y_test))
		print('-------evaluate--------')
		score = model.evaluate(self.X_test, self.y_test, verbose=1)
		print('Test loss:', score[0])
		print('Test accuracy:', score[1])

if __name__ == '__main__':
	d = DNN('minmax')
	d.useKaras()