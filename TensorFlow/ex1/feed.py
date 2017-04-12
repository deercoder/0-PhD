#!/usr/bin/env python
## this example shows how to use `feed` to insert/replace an output, can be used a parameter of run()
import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
	print (sess.run([output], feed_dict={input1:[7.], input2:[2.]}))

# COMMENT
## a placeholder() will provide `feed` operation to be inserted into specific operations
## FOR EXAMPLE, here when run output, it temporary insert the input1 and input2, these
## two placeholder() temporary assigns the value and feed into the operation of output to
## be calculated. (my guess is that it's useful when get output and calculate something)
