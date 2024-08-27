import sys
from PIL import Image, ImageOps
import os

def main():
    file1, file2 = check_args()
    shirt = Image.open("shirt.png")
    try:
        with Image.open(file1) as input_image:
            # 使用 input_image 替换 file
            pro_ima = ImageOps.fit(input_image, shirt.size)
            pro_ima.paste(shirt, mask=shirt)  # mask 应为掩码
            pro_ima.save(file2)

    except FileNotFoundError:
        sys.exit("Invalid input")

def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")

    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Input does not exist")
    else:
        return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    main()
