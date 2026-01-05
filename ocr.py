from PIL import Image

im = Image.open("23a93669523149a78a1d20153fc74610.jpg")
print(im)
print(im.size)
im.show()
im.rotate(90).show()
im.crop((100, 100, 400, 400)).show()
im.save("im_copy.jpg")