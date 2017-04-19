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

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

with tf.Session() as sess:
	sess.run(init)
	for i in range(1000):
		sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})
		print sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]})
	print sess.run([W, b])
