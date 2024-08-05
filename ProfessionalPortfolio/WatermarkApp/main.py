from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
with Image.open("./images/Capture.png") as img:
    img = img.resize((800, 600))  # Adjust the size as needed
    img.save("./images/Capture_resized.png")


font_path = 'Roboto-Regular.ttf'
font_size = 72
myFont = ImageFont.truetype("arial.ttf", 36)
img = Image.open('./images/Capture_resized.png')
I1 = ImageDraw.Draw(img)
I1.text((400, 300),  "Watermark!!", font=myFont, fill=(0, 0, 0))
img.show()
# img.save("./images/Capture_watermarked.png")
