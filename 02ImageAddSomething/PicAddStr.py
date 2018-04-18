from PIL import Image, ImageDraw, ImageFont

def CreateNewPic(weight = 480, height = 480):
    '''Create a new picture as head.Of course you can
    use Image.open('/home/Picture/test.jpg') to open a image,
    and argv3 is change color RGB'''
    return Image.new('RGB', (weight, height), (128, 128, 255))

size = 80   #字体大小
font = ImageFont.truetype('C:/Windows/Fonts/Drummon Outline.ttf', size) #在指定路径打开指定的字体名称（右击属性课）
head = CreateNewPic(400, 400)
draw = ImageDraw.Draw(head)     #对图像操作需要用ImageDraw.Draw将图片设置为可操作对象
draw.text((0,400-size),'1', fill=(255,0,0),font=font)   #在左下角添加1
draw.text((400-size,0),'2', fill=(255,0,0),font=font)   #在右上角添加2
head.show()                                             #显示图片
head.save("head.png","PNG")                             #保存图片
