from PIL import Image, ImageFilter

if __name__ == '__main__':
  # Open Image
  img = Image.open("./FilteredImages/Original/noise_6.tif")
  # Apply Mode Filter with 3x3 Kernel Mask
  img1 = img.filter(ImageFilter.MedianFilter(3))
  # Write out Image
  img1.save('FilteredImages/ModeFilter/noise_6.tif')
