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
|----------|:------------:|------:|---|---|
| acc | 0.955 | 0.949 |  0.956 |

## conclusion

They have almost the same performance

maybe it's because the task is too easy

so there's no difference using deep learning or traditional machine learning