#!/usr/bin/env python

import tensorflow as tf

# Create a constant op and adds as a node into the default graph
matrix1 = tf.constant([[3., 3.]])

## Pay attention to this wrong one, DIMENSION
# matrix1 = tf.constant([3., 3.])

matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)
