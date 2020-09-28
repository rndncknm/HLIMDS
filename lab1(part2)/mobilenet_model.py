import tensorflow as tf

def model(p, num_of_classes): #p-множитель разрешения

  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Conv2D(filters=int(round(32 * p)), padding='same', kernel_size=(3,3), strides=(2, 2), input_shape=(224,224,3), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))

  ########################################################1
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(64 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################1

  ########################################################2
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(2,2)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(128 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################2

  ########################################################3
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(128 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################3

  ########################################################4
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(2,2)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(256 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################4

  ########################################################5
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(256 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################5

  ########################################################6
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(2,2)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(512 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################6

  ########################################################7
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(512 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################7

  ########################################################8
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(512 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################8

  ########################################################9
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(512 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################9

  ########################################################10
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(512 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################10

  ########################################################11
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(512 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################11

  ########################################################12
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(2,2)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(1024 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################12

  ########################################################13
  model.add(tf.keras.layers.DepthwiseConv2D(kernel_size=(3,3), padding='same', depth_multiplier=p, strides=(1,1)))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  model.add(tf.keras.layers.Conv2D(filters=int(round(1024 * p)), padding='same', kernel_size=(1,1), input_shape=(112,112,32), kernel_initializer=tf.keras.initializers.GlorotUniform()))
  model.add(tf.keras.layers.BatchNormalization())
  model.add(tf.keras.layers.ReLU(threshold=6))
  #########################################################13

  model.add(tf.keras.layers.AveragePooling2D(pool_size=(7, 7), strides=(1,1)))
  
  model.add(tf.keras.layers.Flatten())
  
  model.add(tf.keras.layers.Dense(num_of_classes))

  model.add(tf.keras.layers.Softmax()) 

  return model

model = model(1, 1000)
print(model.summary())