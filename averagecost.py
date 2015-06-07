%matplotlib inline
import matplotlib.pyplot as plt#Pythonにおいて数値計算を効率的に行うための拡張モジュール
import pylab as pl
import numpy as np

def f(x,t):             #包絡線のもとの関数を定義
   return x**3/(3*t)+5*t+5



fig, ax = plt.subplots()  # Call the local version, not plt.subplots()
x = np.linspace(2, 15, 100) #xの範囲設定,(下限、上限、〜刻み)
plt.xlim([x.min(),x.max()])   #y軸の範囲
plt.ylim([10,100])
fig.suptitle('Average Cost Curve', fontsize=15)
ax.set_xticks([])   #x,y軸の目盛消し
ax.set_yticks([])
for  t in range(1, 10):  #1~10の範囲でまわす
    y = f(x,t )
    ax.plot(x, y, 'r-', linewidth=1.0, label='sine function', alpha=0.6)

plt.show()
