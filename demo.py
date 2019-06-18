
import tensorflow as tf
a = tf.Variable(3, name='a')
b = tf.Variable(5, name='b')
c = tf.Variable(2, name='c')
d = tf.square(b)
e = tf.multiply(4,a)
f = tf.multiply(e, c)
g = tf.subtract(f, e)
result = tf.square(g)
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    writer = tf.summary.FileWriter('E:\Python\graph', tf.get_default_graph())
    out = sess.run(result)
    print(out)

writer.close()
