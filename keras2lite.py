## Convert keras H5 model to tensorflowlite model
import tensorflow as tf

# Convert the model
converter = tf.lite.TFLiteConverter.from_keras_model(saved_model_dir) # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)