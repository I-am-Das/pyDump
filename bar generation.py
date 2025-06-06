import numpy as np
import matplotlib.pyplot as plt
overs=np.arange(1,11)
score=[3,6,7,18,15,19,5,9,1,16]
plt.bar(overs,score,color='lavender')
plt.title("INDIA score board",color='red')
plt.xlabel("Overs",color='orange')
plt.ylabel("Score",color='blue')
plt.ylabel("Score")
plt.xticks(overs)
plt.grid(axis='y',alpha=0.7)
plt.show()
