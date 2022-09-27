from PIL import Image


def resize_image(size1, size2):
    image = Image.open('picture_name')
    print(f"Current size: {image.size}")
    resize_image = image.resize((size1, size2))
    resize_image.save('image_new_name' + str(size1) + '.jpg')


size11 = int(input("Enter your width: "))
size22 = int(input("Enter your length: "))
resize_image(size11, size22)
