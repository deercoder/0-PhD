#!/usr/bin/env python
import tensorflow as tf

W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)

# create a linear model, y = w * x + b
linear_model = W * x + b

init = tf.global_variables_initializer()
with tf.Session() as sess:
	sess.run(init)
	print sess.run(linear_model, {x:[1,2,3,4]})


## evaluate the model, use y' - y
y = tf.placeholder(tf.float32)
delta = linear_model - y
squared_deltas = tf.square(delta)

# sum all squared errors to create single scalar
loss = tf.reduce_sum(squared_deltas)

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])

with tf.Session() as sess:
	sess.run(init)
	sess.run([fixW, fixb])
	print sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]})
