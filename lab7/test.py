import cv2
import numpy as np
import matplotlib.pyplot as plt

data = np.zeros((128, 128, 3), dtype=np.float32)
gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)


def draw(img, x, y, color):
    img[x, y] = [color, color, color]


draw(data, 5, 5, 100)
draw(data, 6, 6, 100)
draw(data, 5, 6, 255)
draw(data, 6, 5, 255)


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
gray = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
ret, edges = cv2.threshold(sobelx, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
