import cv2

from PIL import Image
img = Image.open('/home/taisei/note/game/cribo.png')
img_resize = img.resize((16, 16))
img_resize.save('/home/taisei/note/game/cribo.png')

img = cv2.imread("/home/taisei/note/game/cribo.png")
white_pixels = (img == (255, 255, 255)).all(axis=-1)
img[white_pixels] = (0, 0, 0)
cv2.imwrite("/home/taisei/note/game/cribo.png", img)
