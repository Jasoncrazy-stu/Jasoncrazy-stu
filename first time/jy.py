{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt             #图表绘图\n",
    "fig = plt.figure(figsize=(6, 4))            #新建图表\n",
    "ax1 = fig.add_subplot(111)    \n",
    "\n",
    "def step_function1(x=''):\n",
    "    if x >0:\n",
    "        return 1\n",
    "    else:\n",
    "        return \n",
    "\n",
    "m = 1\n",
    "print(step_function1(m))\n",
    "\n",
    "x = np.arange(-3.0,3.0,0.001)  \n",
    "y = step_function2(x)\n",
    "\n",
    "ax1.spines['right'].set_color('none')\n",
    "ax1.spines['top'].set_color('none')\n",
    "ax1.xaxis.set_ticks_position('bottom')\n",
    "ax1.spines['bottom'].set_position(('data', 0))\n",
    "ax1.yaxis.set_ticks_position('left')\n",
    "ax1.spines['left'].set_position(('data',0))\n",
    "\n",
    "plt.title(r'$u(t)$') \n",
    "plt.plot(x,y)\n",
    "plt.ylim(-0.1,1.1)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
