from PIL import Image
import os
import string

dir = "F:\\picture\\"           #图片路径

def CheckFileIsPic1(PicDir, Dir = dir):
    #检测打开的文件是否是图片
    if PicDir == None:
        print("Please input picture and directory!")
        return False
    PicDir = dir + PicDir       #文件和路径进行合并
    try:
            Image.open(PicDir).verify()
            return True
    except:
            return False

def CheckFileIsPic2(PicDir, Dir = dir):
    #根据文件名判断是否是文件格式
    if PicDir == None:
        print("Please input picture and directory!")
        return False
    PicDir = dir + PicDir       #文件和路径进行合并
    picFormat = ['.jpg', '.png', '.gif', '.bmp']  # 图片格式,可以人为的添加要处理的格式
    for format in picFormat:
        if (PicDir.rfind(format) >= 0):
            return True
    return False

def ImageScaling(Pic, Ratio = 1):
    #将图片进行等比例的缩放
    weight, height = Pic.size
    new_weight = int(weight * Ratio)
    new_height = int(height * Ratio)
    return Pic.resize((new_weight, new_height),Image.ANTIALIAS)     #图片缩放到指定高宽大小

for file in os.listdir(dir):
    if CheckFileIsPic2(PicDir = file):
        PicFile = Image.open(dir + file)                            #打开图片
        FileFormat = PicFile.format
        PicFile = ImageScaling(PicFile, 2)
        PicFile.save("new_" + file,  FileFormat)                    #保存图片


