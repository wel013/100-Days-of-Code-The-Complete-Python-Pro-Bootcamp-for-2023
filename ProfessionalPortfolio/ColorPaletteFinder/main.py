import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory

app = Flask(__name__)


def extract_colors(image_path, num_colors, resize_dim=(150, 150), batch_size=100, n_init=10):
    # Read the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize the image to the specified dimensions
    image = cv2.resize(image, resize_dim, interpolation=cv2.INTER_AREA)

    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)

    # Perform MiniBatchKMeans clustering
    kmeans = MiniBatchKMeans(n_clusters=num_colors,
                             batch_size=batch_size, n_init=n_init)
    kmeans.fit(pixels)

    # Get the cluster centers (dominant colors)
    colors = kmeans.cluster_centers_

    # Convert the colors to integers
    colors = colors.astype(int)
    print(colors)
    return colors


# def plot_colors(colors):
#     # Create a figure
#     plt.figure(figsize=(8, 6))

#     # Plot each color as a rectangle
#     for i, color in enumerate(colors):
#         plt.subplot(1, len(colors), i + 1)
#         plt.axis('off')
#         plt.imshow(np.ones((100, 100, 3), dtype=np.uint8) * color)

#     plt.show()


# Example usage
image_path = 'static/images/yonezu.jpg'
num_colors = 5  # Number of dominant colors to extract
resize_dim = (150, 150)  # Resize dimensions to speed up processing
colors = extract_colors(image_path, num_colors,
                        resize_dim, batch_size=100, n_init=10)
# plot_colors(colors)


@app.route('/')
def home():
    return render_template("index.html", colors=colors, image=image_path)


if __name__ == "__main__":
    app.run(debug=True)
