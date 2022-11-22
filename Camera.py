from PIL import Image, ImageGrab

num = 0
while True:
    img = ImageGrab.grab()
    img.save("Sequence/ScreenShot" + str(num) + ".bmp", "BMP")
    num += 1