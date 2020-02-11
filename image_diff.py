# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity
import cv2

# import imutils
# import pyautogui
# import argparse

# import pyautogui, time
# import pytesseract as tess

# tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

############# # get the current location of the mouse pointer

"""
# construc the argument parse and parse the arguments
# its used to load the images from the command line interface by using
# this command  # python image_diff.py --first 1.jpg --second 2.jpg
                # python image_diff.py --first 1_1.jpg --second 2_1.jpg

# copy paste these 4 lines of code below and you will be able to use the below commands in the terminal
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image")
ap.add_argument("-s", "--second", required=True, help="second input image")
args = vars(ap.parse_args())

#load two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

"""
# pyautogui.screenshot("name.jpg")
#                     ________  #Point(x=1893, y=206)
#                    |_______| X= 1675
                       #       Y= 5616
                       # starting point Point(x=234, y=108)
                       # OPPORTUNITY screenshot size (x=1675, y=5616)
                       # imageB = imageB[234:1675, 206:5616]
###################################
#                     ________  #Point(x=1893, y=206)
#                    |_______| X= 1690
                       #       Y= 3409
                       # starting point Point(x=234, y=108)
                       # QUOTE screenshot size (x=1675, y=3361)
                       # imageB = imageB[234:1690, 206:3409]
###################################
#                     ________  #Point(x=1893, y=206)
#                    |_______| X= 1675
                       #       Y= 1518
                       # starting point Point(x=234, y=108)
                       # FORECAST screenshot size (x=1675, y=1518)
                       # imageB = imageB[234:1675, 108:1518]
                    
# def get_cursor_possition():
#     position = pyautogui.position()
#     time.sleep(3)
#     print(position)
# get_cursor_possition()



class MarkDifference(object):
    def __init__(self, img1_path, img2_path):
        self.img1_path = img1_path
        self.img2_path = img2_path


    def read_and_change(self):
        imageA = cv2.imread(self.img1_path) # first image before the changes
        imageB = cv2.imread(self.img2_path) # first image that has something changes to it
        # ## get image dimensions
        heightA, widthA, channelsA = imageA.shape
        heightB, widthB, channelsB = imageB.shape
        print(heightA, widthA, channelsA)
        print(heightB, widthB, channelsB)

        # conver the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        #COMPUTE THE STRUCTURAL SIMILARITY INDEX (SSIM) between the two
        # images, ensuring that the difference in the images is returned
        (score, diff) = structural_similarity(grayA, grayB, full=True)
        diff = (diff* 255).astype("uint8")
        print("SSIM: {}".format(score))

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0 , 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0]
        # LOOP OVER THE CONTOURS
        for c in cnts:
            # compute the bounding box of the contour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 1)

        # write a copy of the images to disk
        # cv2.imwrite("1_marked_differences.png", imageA)
        # cv2.imwrite("2_with_marked_differences.png", imageB)
        # cv2.imwrite("Diff.jpg", diff)
        # cv2.imwrite("Thresh.jpg", thresh)

        # show the output images without writing it to disk
        cv2.imshow("Original_with_marked_differences", imageA)
        cv2.imshow("Edited_with_marked_differences", imageB)
        # cv2.imshow("Diff", diff)
        # cv2.imshow("Thresh", thresh)
        cv2.waitKey(0)

if __name__ == "__main__":

# Other images
    img1_path = "C:\\image_recog\\images\\1_4.jpg"
    img2_path = "C:\\image_recog\\images\\2_4.jpg"
    
    b = MarkDifference(img1_path, img2_path)
    b.read_and_change()






############################
############################
############################

### THE CODE WITHOU 
# different show
# # load two input images # opportunity
# img1_path = "C:\image_recog\OP_20028398\OP_20028398.jpg"
# img2_path = "C:\image_recog\OP_20028398\OP_20028398_edited.jpg"
# # load two input images # Forecast
# img1_path = "C:\\image_recog\\OP_20127675\\FO-05125202.jpg"
# img2_path = "C:\\image_recog\\OP_20127675\\FO-05125202_edited.jpg"
# # load two input images # Quote
# img1_path = "C:\\image_recog\\OP_20127675\\Q-01082.jpg"
# img2_path = "C:\\image_recog\\OP_20127675\\Q-01082_edited.jpg"
# imageA = cv2.imread(img1_path) # first image before the changes
# imageB = cv2.imread(img2_path) # first image that has something changes to it

### opportunity image resize
# imageA = imageA[108:5666, 220:1900]
# imageB = imageB[108:5666, 220:1900]

### Forecast image resize
# imageA = imageA[108:1675, 220:1900]
# imageB = imageB[108:1675, 220:1900]

### Quote image resize
# imageA = imageA[108:3409, 220:1900]
# imageB = imageB[108:3409, 220:1900]

### get image dimensions
# heightA, widthA, channelsA = imageA.shape
# heightB, widthB, channelsB = imageB.shape
# print(heightA, widthA, channelsA)
# print(heightB, widthB, channelsB)


## Conver the images to grayscale
# grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
# grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)


### COMPUTE THE STRUCTURAL SIMILARITY INDEX (SSIM) between the two
##  images, ensuring that the difference in the images is returned
# (score, diff) = structural_similarity(grayA, grayB, full=True)
# diff = (diff* 255).astype("uint8")
# print("SSIM: {}".format(score))

### threshold the difference image, followed by finding contours to
## obtain the regions of the two input images that differ
# thresh = cv2.threshold(diff, 0 , 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0]
## LOOP OVER THE CONTOURS
# for c in cnts:
#     ## compute the bounding box of the contour and then draw the
#     ## bounding box on both input images to represent where the two
#     ## images differ
#     (x, y, w, h) = cv2.boundingRect(c)
#     cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)


# imageA = cv2.resize(imageA, (1920, 1080))
# imageB = cv2.resize(imageB, (1920, 1080))

### whrite a copy of the images
# cv2.imwrite("1_marked_differences.png", imageA)
# cv2.imwrite("2_with_marked_differences.png", imageB)
# cv2.imwrite("Diff.jpg", diff)
# cv2.imwrite("Thresh.jpg", thresh)


### show the images
# cv2.imshow("Original_with_marked_differences", imageA)
# cv2.imshow("Edited_with_marked_differences", imageB)
# cv2.imshow("Diff", diff)
# cv2.imshow("Thresh", thresh)
# cv2.waitKey(0)

### different show passing the image into the command line interface
# python image_diff.py --first 1.jpg --second 2.jpg
# python image_diff.py --first 1_1.jpg --second 2_1.jpg

