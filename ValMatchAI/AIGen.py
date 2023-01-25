import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def imageToText(img):
    image = cv2.imread(img)

    cropped_img = image[100:200]
    cv2.imwrite('cropped_out.jpg', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    text = pytesseract.image_to_string(img)

    print(text, 'hi')
