import pyautogui
import  time
from PIL import Image,ImageGrab

def hit(key):
    pyautogui.keyDown(key)
    return

def pixel(data):
    for i in range(360, 480):
        for j in range(380, 460):
            if data[i, j] < 100:
                hit("up")
                return
    # for i in range(450, 480):
    #     for j in range(250, 375):
    #         if data[i, j] < 100:
    #             hit("down")
    #             return

    return
if __name__ == "__main__":
    print("just Switch to chrome and Program will play automatically")
    time.sleep(2)
    # hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data=image.load() #loads pixel data
        pixel(data)
            # hit("up")

        # print(asarray(image))
        # rectangle for cactus
        # for i in range(500, 520):
        #     for j in range(380, 465):
        #         data[i, j] = 0
        # #rectangle for birds
        # for i in range(420, 520):
        #     for j in range(250, 375):
        #         data[i, j] = 71
        #
        # image.show()
        # break
