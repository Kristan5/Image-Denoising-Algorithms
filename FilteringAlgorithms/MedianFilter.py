import numpy as np 
import cv2

def medianFilter(image, filteredImage):
    # Median Filter with 3x3 mask
    # Image Height (y)
    for i in range(1, len(image) - 1):
        # Image Width (x)
        for j in range(1, len(image[1]) - 1):
            window = []
            # Loop through Kernel x 
            for x in range(i - 1, i + 2):
                # Loop through Kernel y
                for y in range(j - 1, j + 2):
                    window.append(image[x][y])
                    
            # Sort Values within appended to window
            window.sort()
            filteredImage[i][j] = window[4]

    return filteredImage

if __name__ == '__main__':
    image = cv2.imread("FilteredImages/Original/noise_7.tif", 0)
    filteredImage = image
    filteredImage = medianFilter(image, filteredImage)
    cv2.imwrite('FilteredImages/MedianFilter/noise_7.tif', filteredImage)

