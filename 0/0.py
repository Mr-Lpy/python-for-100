# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image, ImageFont, ImageDraw

def add_num(img):
    im = Image.open(img)
    w,h = im.size
    font = ImageFont.truetype('C:\Windows\Fonts\simsunb.ttf',50)
    fillColor = "#ff0000"
    draw = ImageDraw.Draw(im)
    draw.text((w-50,20),'1',font=font,fill=fillColor)
    im.save('r.jpg')
    im.show()

if __name__ == '__main__':
    add_num('1.jpg')