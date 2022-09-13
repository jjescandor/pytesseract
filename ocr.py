import cv2
import sys
import pytesseract
from gtts import gTTS
from playsound import playsound

def get_img(img):
    return cv2.imread(img)

image = get_img(sys.argv[1]) 

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = remove_noise(thresholding(get_grayscale(image)))

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def speechify(my_text, language):
    output = gTTS(text=my_text, lang=language, slow=False)
    output.save("audio.mp3")
    playsound("audio.mp3")


if __name__ == "__main__":
    text = ocr_core(img)
    print(text)
    speechify(text, "en")