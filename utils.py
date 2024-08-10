import numpy as np
import imageio

# Example array with shape (3, s, s)
s = 100  # example size
frames = 3
np_array = np.random.randint(0, 255, (frames, s, s), dtype=np.uint8)

# Create a list of images from the array
images = [np_array[i] for i in range(np_array.shape[0])]

imageio.mimsave('output.gif', images, duration=0.5)