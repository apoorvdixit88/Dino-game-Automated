# import PIL #importion pillow package
import pyautogui
import  time
from PIL import Image,ImageGrab




def ss():
    img=ImageGrab.grab()#takes ss
    img.show()
    return  img

if __name__=="__main__":
    time.sleep(2)
    ss()