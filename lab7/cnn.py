import numpy as np
import cv2
from matplotlib import pyplot as plt

# tworzymy tablice o wymiarach 128x128x3 (3 kanaly to RGB)
# uzupelnioną zerami = kolor czarny
data = np.zeros((128, 128, 3), dtype=np.float32)

gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)


# chcemy zeby obrazek byl czarnobialy,
# wiec wszystkie trzy kanaly rgb uzupelniamy tymi samymi liczbami
# napiszmy do tego funkcje
def draw(img, x, y, color):
    img[x, y] = [color, color, color]


# zamalowanie 4 pikseli w lewym górnym rogu
draw(data, 5, 5, 100)
draw(data, 6, 6, 100)
draw(data, 5, 6, 255)
draw(data, 6, 5, 255)


# rysowanie kilku figur na obrazku
for i in range(128):
    for j in range(128):
        if (i-64)**2 + (j-64)**2 < 900:
            draw(data, i, j, 200)
        elif i > 100 and j > 100:
            draw(data, i, j, 255)
        elif (i-15)**2 + (j-110)**2 < 25:
            draw(data, i, j, 150)
        elif (i-15)**2 + (j-110)**2 == 25 or (i-15)**2 + (j-110)**2 == 26:
            draw(data, i, j, 255)

# konwersja macierzy na obrazek i wyświetlenie
plt.imshow(data, interpolation='nearest')
plt.show()


image = tf.constant(data, dtype=tf.float32)

kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])

kernel_tensor = tf.convert_to_tensor(kernel, dtype=tf.float32)
kernel_tensor = tf.reshape(kernel_tensor, [3, 3, 1, 1])
output = tf.nn.conv2d(image[None, :, :, :],
                      kernel_tensor, [1, 1, 1, 1], 'VALID')

kernel = tf.reshape(kernel, [3, 3, 1, 1])

result = tf.squeeze(tf.nn.conv1d(
    data, kernel, 1, padding='VALID'))
