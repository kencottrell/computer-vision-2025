# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('image.jpg')

# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {}, Width = {}".format(h, w))

# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
(B, G, R) = image[100, 100]

# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

# We will calculate the region of interest
# by slicing the pixels of the image
roi = image[100 : 500, 200 : 700]
cv2.imshow("ROI", roi)
cv2.waitKey(1000)

# resize() function takes 2 parameters,
# the image and the dimensions
resize = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(2000)

# redo aspect ratio

# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized Image", resize_aspect)
cv2.waitKey(1000)

# copying the image into a new rectangle
# We are copying the original image,
# as it is an in-place operation.
output = image.copy()

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900),
                        (600, 400), (255, 0, 0), 2)

# display text
# Copying the original image
output = image.copy()

# Adding the text using putText() function
'''It takes in 7 arguments:

Image
Text to be displayed
Bottom-left corner co-ordinates, from where the text should start
Font
Font size
Color (BGR format)
Line width
'''
text = cv2.putText(output, 'OpenCV Demo', (500, 550),
                cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

