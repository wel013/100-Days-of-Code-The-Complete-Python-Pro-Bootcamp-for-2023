import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans, KMeans


def extract_colors(image_path, num_colors, resize_dim=(150, 150), batch_size=100, n_init=10):
    image = cv2.imread(image_path)
    # used to convert an image from one color space to another
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # reduce the size so that the algorithm run faster
    image = cv2.resize(image, resize_dim, interpolation=cv2.INTER_AREA)

    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)

    kmeans = MiniBatchKMeans(n_clusters=num_colors,
                             batch_size=batch_size, n_init=n_init)
    kmeans.fit(pixels)

    # get dominant colors
    colors = kmeans.cluster_centers_

    colors = colors.astype(int)
    # each row is a color
    print(colors)
    return colors


def plot_colors(colors):
    plt.figure(figsize=(8, 6))

    for i, color in enumerate(colors):
        plt.subplot(1, len(colors), i + 1)
        plt.axis('off')
        plt.imshow(np.ones((100, 100, 3), dtype=np.uint8) * color)

    plt.show()

num_colors = int(input("How many color do you want in your palette? "))
image_path = 'sample.jpg'
resize_dim = (150, 150)  # reduce size
colors = extract_colors(image_path, num_colors,
                        resize_dim, batch_size=100, n_init=10)
plot_colors(colors)

