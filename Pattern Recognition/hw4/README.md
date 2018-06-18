# DNN

## code

use a simple DNN network with relu to do classify

also using dropout to prevent overfitting
```python
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
```

## accuracy

| method   |      DNN     | bayes  | knn  |
|----------|:------------:|------:|---|
| acc | 0.955 | 0.949 |  0.956 |

## conclusion

They have almost the same performance

maybe it's because the task is too easy

so there's no difference using deep learning or traditional machine learning

## TO DO

1. Using relu as activation function can only get Testing Accuracy: 0.37078652
	```python
	# Parameters
	learning_rate = 0.1
	batch_size = 4
	epoch = 1000
	num_steps = int(epoch * len(self.X_train) / batch_size)
	display_step = 100
	# tf Graph input
	X = tf.placeholder("float", [None, 13])
	Y = tf.placeholder("float", [None, 3])
	layer_1 = tf.layers.dense(X, 256, activation=tf.nn.relu)
	out_layer = tf.layers.dense(layer_1, 3, activation=tf.nn.relu)
	prediction = tf.nn.softmax(out_layer)
	```
2. But just remove the activation function and turn it into linear model: Testing Accuracy: 0.8988764
	```python
	# Parameters
	learning_rate = 0.1
	batch_size = 4
	epoch = 1000
	num_steps = int(epoch * len(self.X_train) / batch_size)
	display_step = 100
	# tf Graph input
	X = tf.placeholder("float", [None, 13])
	Y = tf.placeholder("float", [None, 3])
	layer_1 = tf.layers.dense(X, 256)
	out_layer = tf.layers.dense(layer_1, 3)
	prediction = tf.nn.softmax(out_layer)
	```
3. Removing activation function of output layer: 0.94382024
	```python
	# Parameters
	learning_rate = 0.1
	batch_size = 4
	epoch = 1000
	num_steps = int(epoch * len(self.X_train) / batch_size)
	display_step = 100
	# tf Graph input
	X = tf.placeholder("float", [None, 13])
	Y = tf.placeholder("float", [None, 3])
	layer_1 = tf.layers.dense(X, 256, activation=tf.nn.relu)
	out_layer = tf.layers.dense(layer_1, 3)
	prediction = tf.nn.softmax(out_layer)
	```
4. Or, we can insist using relu and use smaller learning (to be noticed that learning_rate cannot be too small, or it would stuck at local minimum. You can reduce the risk of getting stuck in a local minima by adopting a larger learning rate in the beginning and shrinking it over time) rate and bigger epoch:  Testing Accuracy: 0.9325843
	```python
	# Parameters
	learning_rate = 0.0001
	batch_size = 4
	epoch = 50000
	num_steps = int(epoch * len(self.X_train) / batch_size)
	display_step = 100
	# tf Graph input
	X = tf.placeholder("float", [None, 13])
	Y = tf.placeholder("float", [None, 3])
	layer_1 = tf.layers.dense(X, 256, activation=tf.nn.relu)
	out_layer = tf.layers.dense(layer_1, 3, activation=tf.nn.relu)
	prediction = tf.nn.softmax(out_layer)
	```