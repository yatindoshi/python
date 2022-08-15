import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

n = 200
D = np.zeros((n, 2))
D[:, 0] = np.linspace(0, 10, n) + np.random.randn(n)
D[:, 1] = D[:, 0] ** 2 + np.random.randn(n) * 10
sns.jointplot(D[:, 0], D[:, 1])
plt.show()

df = pd.DataFrame(data=D, columns=['var1', 'var2'])
sns.jointplot(df.columns[0], df.columns[1], data=df)
plt.show()
