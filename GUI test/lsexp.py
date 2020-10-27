import numpy as np
import matplotlib.pyplot as plt
n=np.arange(0,15)
a=3.0/4
f=a**n
plt.subplot(221)
plt.title(u'a=3/4')
plt.stem(n,f)
a=-3.0/4
f=a**n
plt.subplot(222)
plt.title(u'a=-3/4')
plt.stem(n,f)
a=5.0/4
f=a**n
plt.subplot(223)
plt.title(u'a=5/4')
plt.stem(n,f)
a=-5.0/4
f=a**n
plt.subplot(224)
plt.title(u'a=-5/4')
plt.stem(n,f)
plt.show()
