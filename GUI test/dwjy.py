import numpy as np
from matplotlib import pyplot as plt
from DSP import *
a=impseq(1,0,10)
b=stepseq(1,0,10)
n=np.arange(0,11)
print(a)
print(b)
print(n)
plt.subplot(2,1,1)
plt.stem(n,a,use_line_collection=False)
plt.show()