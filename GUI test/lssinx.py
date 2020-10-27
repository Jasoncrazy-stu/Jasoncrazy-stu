# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,5,20)
x1=np.linspace(1,10,10)
X=[2,1.5,1,0.5]
y1=[]
for i in range(32):
      y1.append(X[i%4])
#fig=plt.figure('16010140048') #加入网格线的内容

y2=2*np.sin(0.5*np.pi*x+2)
plt.title('sinx')
#plt.grid(True) #是否生成网格线
plt.stem(x,y2)

plt.show()
