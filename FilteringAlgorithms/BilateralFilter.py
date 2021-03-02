import cv2

if __name__ == '__main__':
  # Importing file
  image = cv2.imread("FilteredImages/Original/noise_6.tif", 0)
  filteredImage = image
  # bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None, /) -> dst
  # Using opencv's bilateral filter with a 5x5 kernel mask, 100 sigma color, and 200 sigma space
  filteredImage = cv2.bilateralFilter(image, 5, 100, 200, borderType=cv2.BORDER_CONSTANT)
  # Writing out
  cv2.imwrite('FilteredImages/BilateralFilter/noise_6.tif', filteredImage)
