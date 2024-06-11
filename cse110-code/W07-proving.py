from PIL import Image
img_1 = Image.open("Images/earth.jpg")
pix_1 = img_1.load()
img_2 = Image.open("Images/penguin.jpg")
pix_2 = img_2.load()
width1, height1 = img_2.size
width2, height2 = img_1.size
for h in range(0, height2):
    for w in range(0, width2):
        r,g,b = pix_1[w,h]
        r2,g2,b2 = pix_2[w,h]
        if g2 > 150 and r2 < 110 and b2 < 110:
            pix_2[w,h] = (r,g,b)
img_2.show()

