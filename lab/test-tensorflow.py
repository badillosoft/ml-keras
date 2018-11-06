import tensorflow as tf

with tf.Session():
    x = tf.constant(1, shape=(4, ))
    result = x.eval()
    print(result)