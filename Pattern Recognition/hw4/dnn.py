from sklearn.preprocessing import Normalizer, MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas
import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
import tensorflow as tf

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

		# for tensorflow
		self.sess = tf.InteractiveSession()


	def useTf(self):
		# Parameters
		learning_rate = 0.00001
		batch_size = 4
		epoch = 1000
		num_steps = int(epoch * len(self.X_train) / batch_size)
		display_step = 100

		# tf Graph input
		X = tf.placeholder("float", [None, 13])
		Y = tf.placeholder("float", [None, 3])
		isTrain = tf.placeholder(tf.bool, shape=())

		layer_1 = tf.layers.dense(X, 512, activation=tf.nn.relu)
		drop_1 = tf.layers.dropout(layer_1, rate=0.5, training=isTrain)
		layer_2 = tf.layers.dense(drop_1, 512, activation=tf.nn.relu)
		drop_2 = tf.layers.dropout(layer_2, rate=0.5, training=isTrain)
		layer_3 = tf.layers.dense(drop_2, 512, activation=tf.nn.relu)
		drop_3 = tf.layers.dropout(layer_3, rate=0.5, training=isTrain)
		out_layer = tf.layers.dense(drop_3, 3)
		prediction = tf.nn.softmax(out_layer)

		# Define loss and optimizer
		loss_op = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=out_layer, labels=Y))
		optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
		train_op = optimizer.minimize(loss_op)

		# Evaluate model
		correct_pred = tf.equal(tf.argmax(prediction, axis=1), tf.argmax(Y, axis=1))
		accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

		# Initialize the variables (i.e. assign their default value)
		self.sess.run(tf.global_variables_initializer())
		for step in range(num_steps):
			# batch_x, batch_y = tf.train.shuffle_batch(
			#   [X_train, y_train],
			#   batch_size=3,
			#   num_threads=1,
			#   capacity=10,
			#   enqueue_many=True,
			#   allow_smaller_final_batch=True,
			#   min_after_dequeue=4)
			# Run optimization op (backprop)
			choose = int(np.random.rand() * len(self.X_train))
			batch_x, batch_y = np.array(self.X_train[choose:choose+batch_size]), np.array(self.y_train[choose:choose+batch_size])
			self.sess.run(train_op, feed_dict={X: batch_x, Y: batch_y, isTrain:True})
			if step % display_step == 0 or step == 1:
				# Calculate batch loss and accuracy
				loss, acc = self.sess.run([loss_op, accuracy], feed_dict={X: batch_x, Y: batch_y, isTrain:True})
				print("Step " + str(step) + ", Minibatch Loss= " + str(loss) + ", Training Accuracy= " + str(acc))


		print("Optimization Finished!")
		# Calculate accuracy for MNIST test images
		print("Testing Accuracy:", self.sess.run(accuracy, feed_dict={X: self.X_test, Y: self.y_test, isTrain:False}))
		self.sess.close()

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
	d.useTf()
	d.useKaras()