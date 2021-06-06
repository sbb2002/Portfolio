#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

data = pd.read_csv(r'.\data\raw.csv', sep=',')
data

# %%
data.info()
# %%
# null-counting
sns.heatmap(data.isnull(), cbar=False)

# %%
import missingno as msno

msno.matrix(data.sample(250))
# %%
msno.bar(data.sample(1000))
# %%
msno.heatmap(data)
# %%
msno.dendrogram(data)
# %%
# Delete the null: Deletion
# axis=0 (row) / axis=1 (col) / how="any" (del those cells of that raw/col)
# inplace=T (overwrite at pd, but show)
data.dropna(axis=0, how='any', inplace=True)
data

# %%
# Go for tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from pandas.io.parsers import read_csv

model = tf.global_variables_initializer()

#%%
data.replace("소한", 0, inplace=True)
#%%
data.replace("대한", 1, inplace=True)
#%%
data.replace("입춘", 2, inplace=True)
#%%
data.replace("우수", 3, inplace=True)
#%%
data.replace("경칩", 4, inplace=True)
#%%
data.replace("춘분", 5, inplace=True)
#%%
data.replace("청명", 6, inplace=True)
#%%
data.replace("곡우", 7, inplace=True)
#%%
data.replace("입하", 8, inplace=True)
#%%
data.replace("소만", 9, inplace=True)
#%%
data.replace("망종", 10, inplace=True)
#%%
data.replace("하지", 11, inplace=True)
#%%
data.replace("소서", 12, inplace=True)
#%%
data.replace("대서", 13, inplace=True)
#%%
data.replace("입추", 14, inplace=True)
#%%
data.replace("처서", 15, inplace=True)
#%%
data.replace("백로", 16, inplace=True)
#%%
data.replace("추분", 17, inplace=True)
#%%
data.replace("한로", 18, inplace=True)
#%%
data.replace("상강", 19, inplace=True)
#%%
data.replace("입동", 20, inplace=True)
#%%
data.replace("소설", 21, inplace=True)
#%%
data.replace("대설", 22, inplace=True)
#%%
data.replace("동지", 23, inplace=True)

#%%
data

#%%
# correlation
data.corr()

#%%
# visualize the corr() by heatmap
plt.figure(figsize=(15,15))
sns.heatmap(data = data.corr(), annot=True, fmt='.2f', linewidths=.5, cmap='Blues')
# %%
xy = np.array(data, dtype=np.float32)
xy

# %%
x_data = xy[:, 1:-1]    # [ all rows, cols="date / season / avgTemp / maxTemp / minTemp / rainfall / interest" ]
y_data = xy[:, [-1]]    # [ all rows, col="cost"]

# %%
X = tf.placeholder(tf.float32, shape=[None, 6]) # season / avg / maxT / minT / rain
Y = tf.placeholder(tf.float32, shape=[None, 1]) # cost
W = tf.Variable(tf.random_normal([6, 1]), name="weight") # 각 X 변수들의 기울기
b = tf.Variable(tf.random_normal([1]), name="bias") # 각 X 변수들에 대한 바이어스

# %%
hypothsis = tf.matmul(X, W) + b

# %%
cost = tf.reduce_mean(tf.square(hypothsis - Y))

# %%
optmizer = tf.train.GradientDescentOptimizer(learning_rate=0.000007)    #default rate=0.000005 (not good)

# %%
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
saver = tf.train.Saver()
save_path = saver.save(sess, "./model_lr/saved.cpkt")
print("학습된 모델을 저장했습니다.")

# %%
