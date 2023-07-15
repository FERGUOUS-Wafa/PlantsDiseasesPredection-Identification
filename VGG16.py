from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten, Dense, BatchNormalization, Dropout
from tensorflow.keras.models import Sequential

inputShape = (height, width, depth)

# Load the pre-trained VGG16 model
base_model = VGG16(weights='imagenet', include_top=False, input_shape=inputShape)

# Freeze the pre-trained layers
for layer in base_model.layers:
    layer.trainable = False

# Create a new model
model = Sequential()

# Add the VGG16 base model
model.add(base_model)

# Add additional layers on top of VGG16
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(n_classes, activation='softmax'))

model.summary()
from tensorflow.keras.optimizers import Adam
import tensorflow as tf

learning_rate = 0.001
decay = learning_rate / EPOCHS
opt = tf.keras.optimizers.legacy.Adam(learning_rate=learning_rate, decay=decay)

model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
history = model.fit(
    aug.flow(x_train, y_train, batch_size=BS),
    validation_data=(x_test, y_test),
    steps_per_epoch=len(x_train) // BS,
    epochs=25,
    verbose=1
)

# Obtain the training and validation accuracy and loss
train_loss = history.history['loss']
train_accuracy = history.history['accuracy']
val_loss = history.history['val_loss']
val_accuracy = history.history['val_accuracy']

# Print the final validation loss and accuracy
print("Final Validation Loss:", val_loss[-1])
print("Final Validation Accuracy:", val_accuracy[-1])

# Obtain the training and validation accuracy and loss
train_loss = history.history['loss']
train_accuracy = history.history['accuracy']
val_loss = history.history['val_loss']
val_accuracy = history.history['val_accuracy']

# Print the final validation loss and accuracy
print("Final Validation Loss:", val_loss[-1])
print("Final Validation Accuracy:", val_accuracy[-1])

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Get predicted labels from the model
y_pred = model.predict(x_test)
y_pred = np.argmax(y_pred, axis=1)  # Convert probabilities to class labels
y_true = np.argmax(y_test, axis=1)

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Get label names
label_names = label_binarizer.classes_

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Greens', fmt='d', xticklabels=label_names, yticklabels=label_names)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
