# This code is an implementation of the noisy image comparison metric described in the paper
# Rank, K., Landl, M., Unbehauen, R., “Estimation of image noise variance”, IEE Proceedings Vision,
# Image and Signal Processing, Vol.146, pp.80-84 (1999) 
# Available at: http://pdf.xuebalib.com:1262/xuebalib.com.34230.pdf

import math
import cv2
from statistics import variance, mean

def rankDifference(image, filteredImage):
  for i in range(1, len(image) - 1):
    # Image Width (x)
    for j in range(1, len(image[1]) - 1):
      # Difference operator vertically across rows
      filteredImage[i][j] = (1/math.sqrt(2))*(image[i+1][j] - image[i][j])
      # Difference operator horizontally across columns
      filteredImage[i][j] = (1/math.sqrt(2))*(image[i][j+1] - image[i][j])

  return filteredImage

def localStdDevHist(image, filteredImage):
  # 3x3 sized window N = L^2
  L = 3
  N = L**2
  for i in range(1, len(image) - 1):
    # Image Width (x)
    for j in range(1, len(image[1]) - 1):
      window = []
      # Loop through Kernel x for 3x3 window
      for x in range(i - 1, i + L-1):
        # Loop through Kernel y for 3x3 window
        for y in range(j - 1, j + L-1):
          # Apply operation specified in Rank paper
          image[x][y] = image[x][y] - N * mean([i,j])**2
          window.append(image[x][y])

    filteredImage[i][j] = 1/(N-1) * window[4]

  return filteredImage

def histogramEvaluation(image, filteredImage):
  imageArr = []
  for i in range(1, len(image) - 1):
    # Image Width (x)
    for j in range(1, len(image[1]) - 1):
      imageArr.append(image[i])
      imageArr.append(image[i][j])

  imageToList = image[1].tolist()

  return variance(imageToList)

if __name__ == '__main__':
  files = ['FilteredImages/ModeFilter/noise_6.tif', 'FilteredImages/MedianFilter/noise_6.tif', 'FilteredImages/BilateralFilter/noise_6.tif']
  for i in range(3):
    image = cv2.imread(files[i], 0)
    filteredImage1 = image
    filteredImage1 = rankDifference(image, filteredImage1)
    filteredImage2 = filteredImage1
    filteredImage2 = localStdDevHist(filteredImage1, filteredImage2)
    filteredImage = filteredImage2
    filteredImage = histogramEvaluation(filteredImage2, filteredImage)
    print("Image Noise Variation: ", filteredImage)
    # cv2.imwrite('FilteredImages/rankNoise_1.jpg', filteredImage)
