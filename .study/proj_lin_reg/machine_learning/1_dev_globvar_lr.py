# cmd에서 작업 시 dataset.csv의 경로로 이동해 jupyter notebook 실행할것

#%%
import tensorflow.compat.v1 as tf
import numpy as np
from pandas.io.parsers import read_csv
tf.disable_v2_behavior()

model = tf.global_variables_initializer()
data = read_csv('dataset.csv', sep=',')     # 첫 col 제외하고 모두 int일 것!

xy = np.array(data, dtype=np.float32)

# %%
# 자료... (????)
print(xy)

# %%
x_data = xy[:, 1:-1]    # [ all rows, cols="date / avgTemp / maxTemp / minTemp / rainfall" ]
y_data = xy[:, [-1]]    # [ all rows, col="cost"]

'''
*** Slicing gramma ***
# slicing gramma = [ start(이상) : end(미만) : step(1) ]
# 각 idx는 [처음부터]0 1 2 3 ... / ... -4 -3 -2 -1[끝부터] 이 가능함.
# ,(comma)가 들어가면 dimension 구분을 함. --> row / col
'''

# %%
X = tf.placeholder(tf.float32, shape=[None, 4]) # avg / M / m / rain
Y = tf.placeholder(tf.float32, shape=[None, 1]) # cost
W = tf.Variable(tf.random_normal([4, 1]), name="weight") # 각 X 변수들의 기울기
b = tf.Variable(tf.random_normal([1]), name="bias") # 각 X 변수들에 대한 바이어스

# %%
# 가설 공식 ( 행렬 공식 )
hypothsis = tf.matmul(X, W) + b

# %%
cost = tf.reduce_mean(tf.square(hypothsis - Y))
# %%
optmizer = tf.train.GradientDescentOptimizer(learning_rate=0.0011)    #default rate=0.000005 (not good)
# 0.001 ~ 0.0005 = +-500원 차이남
train = optmizer.minimize(cost)

# %%
sess = tf.Session()
sess.run(tf.global_variables_initializer())
# %%
for step in range(100001):
    cost_, hypo_, _ = sess.run([cost, hypothsis, train], feed_dict={X: x_data, Y: y_data})
    if step % 500 == 0:
        print("#", step, "\t손실비용: ", cost_)
        print("- 배추가격: ", hypo_[0])
# %%
# 학습완료된 모델 저장하기
saver = tf.train.Saver()
save_path = saver.save(sess, "./saved.cpkt")
print("학습된 모델을 저장했습니다.")
# %%
# checkpoint
# saved.cpkt.* x 3
# 이것을 이용해서 예측된 배추가격을 내보낼 수 있음 ^^
# %%
