#%%
import tensorflow.compat.v1 as tf
import numpy as np
tf.disable_v2_behavior()


# %%
X = tf.placeholder(tf.float32, shape=[None, 6]) # avg / M / m / rain / int
Y = tf.placeholder(tf.float32, shape=[None, 1]) # cost
W = tf.Variable(tf.random_normal([6, 1]), name="weight") # 각 X 변수들의 기울기
b = tf.Variable(tf.random_normal([1]), name="bias") # 각 X 변수들에 대한 바이어스

# %%
hypothsis = tf.matmul(X, W) + b

# %%
saver = tf.train.Saver()
model = tf.global_variables_initializer()

# %%
season = float(input('현재절기 지수: '))  # project.txt 참조
avgTemp = float(input('평균 온도: '))
minTemp = float(input('최저 온도: '))
maxTemp = float(input('최고 온도: '))
rain_fall = float(input('강수량: '))
interest = float(input('현재 금리: '))

# %%
with tf.Session() as sess:
    sess.run(model)

    save_path = "../model_lr/saved.cpkt"
    saver.restore(sess, save_path)

    data = ((season, avgTemp, minTemp, maxTemp, rain_fall, interest), )
    arr = np.array(data, dtype=np.float32)

    x_data = arr[0:5]
    dict_p = sess.run(hypothsis, feed_dict={X: x_data})
    print(dict_p[0])
# %%
