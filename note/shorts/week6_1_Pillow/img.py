from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("pic.jpeg") as image_:
        print(image_.size)
        print(image_.format)
        img = image_
        '''
        img = image_.rotate(180)
        img.save("旋转.png")
        #旋转180deg
        '''
        new_img = img.filter(ImageFilter.GaussianBlur)
        #Gauss Blur
        new_img.save("out.png")
        edge_img = img.filter(ImageFilter.FIND_EDGES)
        edge_img.save("Edges_image.png")

main()