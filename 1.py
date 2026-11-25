from PIL import Image,ImageFont,ImageDraw,ImageEnhance,ImageFilter,ImageOps
img=Image.open('apple.png')
#img.show()
image = img.convert("RGB")
image.save('save.jpg',format='JPEG')
'''
with Image.open("photo.jpg") as img:
    img.save("out.png")
'''
print(img.format)
print(img.size) #عرض و ارتفاع
print(img.width,img.height)
print(img.mode) #RGB
'''
مد	توضیح
RGB	رنگی (قرمز، سبز، آبی)
RGBA	رنگی با کانال شفافیت
L	سیاه‌وسفید (خاکستری)
1	فقط سیاه و سفید خالص
CMYK	مناسب چاپ

'''

'''
# اندازه دقیق (ممکن است نسبت تصویر به‌هم بخورد)
small = img.resize((400, 300))

# حفظ نسبت تصویر (تغییر روی خود تصویر انجام می‌شود)
img.thumbnail((400, 400))

# کیفیت بهتر با فیلتر
small = img.resize((400, 300), Image.Resampling.LANCZOS)
'''
cropped = image.crop((100, 50, 400, 300))
cropped.save("cropped.jpg")
rotated = img.rotate(45)                  # چرخش پادساعتگرد
rotated = img.rotate(45, expand=True)     # بزرگ شدن بوم تا چیزی بریده نشود
rotated = img.rotate(90, expand=True, fillcolor="white")

flipped_h = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)  # قرینه افقی
flipped_v = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)  # قرینه عمودی
# بوم سفید ۵۰۰×۳۰۰
canvas = Image.new("RGB", (500, 300), "white")
canvas.save('1.jpg')
# با رنگ دلخواه (RGB)
canvas = Image.new("RGB", (500, 300), (255, 100, 50))
canvas.save('2.jpeg')
# بوم شفاف
transparent = Image.new("RGBA", (500, 300), (0, 0, 0, 0))
transparent.save('3.png')
background = Image.open("2.jpg")
logo = Image.open("apple.png").convert("RGBA")

# استفاده از خود لوگو به عنوان ماسک (برای حفظ شفافیت)
background.paste(logo, (50, 50), logo)
background.save("result.jpg")
'''
font = ImageFont.truetype()
img = Image.new("RGB", (600, 400), "white")
draw = ImageDraw.Draw(img)
draw.text((50, 300), "Hello Pillow!", fill="black", font=font)

img.save("drawing.png")
'''
brighter = ImageEnhance.Brightness(img).enhance(1.5)
contrast = ImageEnhance.Contrast(img).enhance(1.3)
color    = ImageEnhance.Color(img).enhance(0.5)      # کم‌رنگ‌تر
sharper  = ImageEnhance.Sharpness(img).enhance(2.0)


blur = img.filter(ImageFilter.BLUR)
gaussian = img.filter(ImageFilter.GaussianBlur(radius=5))
sharp = img.filter(ImageFilter.SHARPEN)
edges = img.filter(ImageFilter.FIND_EDGES)
contour = img.filter(ImageFilter.CONTOUR)
emboss = img.filter(ImageFilter.EMBOSS)

from PIL import ImageOps

ImageOps.grayscale(img)              # خاکستری
ImageOps.invert(img.convert("RGB"))  # منفی
ImageOps.mirror(img)                 # قرینه افقی
ImageOps.flip(img)                   # قرینه عمودی
ImageOps.autocontrast(img)           # کنتراست خودکار
ImageOps.equalize(img)               # یکنواخت‌سازی هیستوگرام
ImageOps.expand(img, border=20, fill="black")   # قاب
ImageOps.fit(img, (300, 300))        # برش و تغییر اندازه هوشمند به اندازه دقیق
ImageOps.exif_transpose(img)         # اصلاح چرخش عکس موبایل

img.save("a.jpg", quality=85, optimize=True)   # JPEG
img.save("a.png", optimize=True)               # PNG
img.save("a.webp", quality=80)                 # WebP

'''
ساخت گیف
frames = [Image.open(f"frame{i}.png") for i in range(1, 6)]
frames[0].save("anim.gif", save_all=True, append_images=frames[1:],
               duration=200, loop=0)   # duration به میلی‌ثانیه
               
'''