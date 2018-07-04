"""Script to call the background-removal API with an image.

USAGE: python test.py static/bird.jpg
"""
import firefly
import sys
import shutil
import base64

background_removal = firefly.Client("https://test-background-removal.rorocloud.io")

def main():
    image_path = sys.argv[1]
    # format = image_path.split(".")[-1]
    # print(image_path)

    print("calling the background removal API...")
    new_image = background_removal.predict(image=image_path)

    ## To open Image using PIL
    # from PIL import Image
    # img = Image.open(new_image)
    img_decode = base64.b64decode(new_image["data"])
    with open("output.png", "wb") as f:
        f.write(img_decode)
    print("saved the output image in output.jpg")

if __name__ == '__main__':
    main()
