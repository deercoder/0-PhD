#!/usr/bin/env python
### how to fetch the result from output

import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

intermd = tf.add(input2, input3)

mul = tf.multiply(input1, intermd)

with tf.Session() as sess:
	result = sess.run([mul, intermd])
	print result

#COMMENT:
## In this example, they show how to fetch multiple data as one tensor, the result contains mul and intermd, 
## we can just assign to result and get them, later using CNN, we can store the temporary result and update
## this way it shows how to get the results

## COMMENT2:
## according to tensorflow v1.0, interface has changed,
## tf.mul, tf.sub and tf.neg are deprecated in favor of tf.multiply, tf.subtract and tf.negative.
