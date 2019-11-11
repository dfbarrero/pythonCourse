from PIL import Image

size = (128, 128)

im =  Image.open("africa.tif")
im.thumbnail(size)
im.save("africa.jpg")
im.show()
