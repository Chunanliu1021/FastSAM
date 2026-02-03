import cv2
from PIL import Image
import time

pic_name = "test"
try:
    img = Image.open(pic_name + ".jpg")
    img = img.resize((640, 480), Image.ANTIALIAS)
    img.save(pic_name + ".jpg")
except:
    img = Image.open(pic_name + ".png")
    img = img.convert("RGB")
    img = img.resize((640, 480), Image.ANTIALIAS)
    img.save(pic_name + ".jpg")

global i, w, h
i = 1
w = 0
h = 0
# 定义回调函数
def mouse_callback(event, x, y, flags, param):
    global i, w, h
    if event == cv2.EVENT_LBUTTONDOWN:
        print('鼠标左键单击：')
        print('坐标：', x, y)
        print('像素值：', img[y, x])
        if(i == 1):
            w = x
            h = y
        elif(i == 2):
            w = x-w
        elif(i == 3):
            h = y-h
            print("!!!!!!!!!!!!!!!!!!!!")
            print("w*h : {}*{}".format(w, h))
        i = i+1
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow('image', img)
# 读取图像
img = cv2.imread(pic_name +'.jpg')

# 显示图像
cv2.imshow('image', img)

# 注册回调函数
cv2.setMouseCallback('image', mouse_callback)

# 循环等待按键
while True:
    key = cv2.waitKey(0) & 0xFF
    # 按下 'q' 键退出
    if key == ord('q'):
        break
# 关闭窗口
cv2.destroyAllWindows()
