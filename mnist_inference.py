import tensorflow as tf
import keras
from keras.models import load_model

model = load_model("test.h5")

import numpy as np
img = np.random.rand(1, 28, 28, 1)  # Change this to whatever it expects as the input tensor

# Set up trace for operations
run_metadata = tf.RunMetadata()
run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)

# The optimizer and loss don't matter since we are doing inference.
#  So just choose anything for optimizer and loss.
model.compile(optimizer=keras.optimizers.Adam(), loss='mse',
    options=run_options,
    run_metadata=run_metadata)

from keras_predict import predict_fn
predict_fn(model, run_metadata)

