#coding=utf-8
#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageDraw, ImageFont

ttfont = ImageFont.truetype("simkai.ttf", 20)

imgStr = "C:/Users/heheda/Desktop/pb图片/ak.jpg"
newImg = "C:/Users/heheda/Desktop/pb图片/ak2.jpg"

img = Image.open(unicode(imgStr, "utf-8"))

draw = ImageDraw.Draw(img)

out = img.resize((100, 100))

# draw.text((10, 10), u'韩寒', fill=(0, 0, 0), font=ttfont)
# draw.text((40, 40), unicode('杨利伟', 'utf-8'), fill=(0, 0, 0), font=ttfont)
out.show()

out.save(unicode(newImg, "utf-8"))
