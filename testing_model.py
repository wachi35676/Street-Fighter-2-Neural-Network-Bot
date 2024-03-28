import tensorflow.keras.models as models
import numpy as np

# Load the model
loaded_model = models.load_model('model.h5')

# Assume that you have a new row of data as a numpy array, called `new_data_row`
new_data_row = np.array([
    0, 0, 85, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 210, 267, 0, 0, 0
])

# Reshape the new data row to have a single sample with the appropriate number of features
new_data_row = new_data_row.reshape(1, -1)

# Make a prediction with the loaded model
prediction = loaded_model.predict(new_data_row)

# Print the prediction
print('Prediction:', prediction[0])

# print only the prediction value
print('Prediction Value:', prediction[0][0])
