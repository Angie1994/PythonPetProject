from PIL import Image
import os
import time


dir = "F:\picture"                                  #图片路径
picFormat = ['.jpg', '.png', '.gif', '.bmp']        #图片格式

for a in os.listdir(dir):
    print("a:%d"%a.find(picFormat[0]))
    if a.rfind(picFormat[0]) > 0:
        print("%s"%a)
        pic = Image.open(dir + '\\' + a)
        pic.show()
        time.sleep(3)
