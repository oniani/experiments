"""
A basic LinearRegressor pattern in TensorFlow
"""


import numpy as np
import tensorflow as tf
from tensorflow import estimator


# Create feature column and estimator
column            = tf.feature_column.numeric_column('col')
linear_regression = tf.estimator.LinearRegressor(feature_columns=[column])

# Train the estimator
train_input = tf.estimator.inputs.numpy_input_fn(
    x={'col': np.array(range(1, 11))},
    y=np.array(range(11, 21)), shuffle=False, num_epochs=None)
linear_regression.train(train_input, steps=2500)  # 2500 training iterations

# Make two predictions
predict_input = tf.estimator.inputs.numpy_input_fn(
     x={'col': np.array([9.2, 11.4], dtype=np.float32)},
     num_epochs=1, shuffle=False)
results = linear_regression.predict(predict_input)

# Print result
for result in results:
    print(result['predictions'])
