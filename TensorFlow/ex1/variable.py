#!/usr/bin/env python
import tensorflow as tf

state = tf.Variable(0, name="counter")

one = tf.constant(1)
new_value = tf.add(state, one)

# define the op, or rules to update/assign value
update = tf.assign(state, new_value)

## Variables MUST be initilized by running the `init` op
init_op = tf.initialize_all_variables()

with tf.Session() as sess:
	# run the `init` op
	sess.run(init_op)
	# print the initial value of state
	print (sess.run(state))
	
	# run the op that update the `state` and print it out
	for _ in range(3):
		sess.run(update)
		print (sess.run(state))
