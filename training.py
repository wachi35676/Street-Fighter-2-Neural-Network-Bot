import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Read in the data from the CSV file
df = pd.read_csv('game_data.csv')

# Split the data into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2)

# Define the input and output variables for the model
X_train = train_data.iloc[:, :-1].values
y_train = train_data.iloc[:, -1].values
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# Define the neural network model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)

# Print the accuracy
print('Accuracy: %.2f' % (accuracy * 100))

# Print the loss
print('Loss: %.2f' % (loss * 100))

# Save the model
model.save('model.h5')
