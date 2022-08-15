import matplotlib.pyplot as plt
import numpy as np
from imageio.v3 import imread

m = 3
n = 5
matrix = np.random.randint(10, size=(m, n))

# plt.plot(matrix)
# plt.show()

# plt.imshow(matrix)
# plt.colorbar()
# plt.show()

image = imread("/users/yatin/Downloads/yatin.jpeg")
print(image.shape)
plt.imshow(image)
plt.colorbar()
plt.show()
