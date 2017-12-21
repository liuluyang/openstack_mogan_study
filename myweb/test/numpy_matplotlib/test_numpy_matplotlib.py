import matplotlib.pyplot as plt
import numpy as np

y=[2000,1000,3000,2500,1500]

index=np.arange(3,8)
print index

plt.bar(left=index,height=y,color='green',width=0.5)

plt.show()