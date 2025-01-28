#file to create dummy image for chat

from PIL import Image

img = Image.new("RGB", (224, 224), (255, 255, 255))  # white background, 224×224
img.save("dummy.png")