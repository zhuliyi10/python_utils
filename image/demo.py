
from PIL import Image
import sys
import os
parent_path = os.path.dirname(__file__)
resutlt_path=os.path.join(parent_path,'result')

def fill_image(image):
    """
    #将图片填充为正方形
    """
    width, height = image.size
    square = width if width > height else height
    new_image = Image.new(image.mode, (square, square), color='white')

    new_image.paste(image, (int((square-width)/2), int((square-height)/2)))

    return new_image

def cut_image(image):
    """
    剪裁图片
    """
    width,height=image.size
    item_size=int(width/3)
    box_list=[]
    for i in range(3):
        for j in range(3):
            box=(item_size*j,item_size*i,item_size*(j+1),item_size*(i+1))
            box_list.append(box)
    return [image.crop(box)for box in box_list]

def save_image(image_list):
    if not os.path.exists(resutlt_path):
        os.mkdir(resutlt_path)
    
    for i,image in enumerate(image_list):
        image.save(os.path.join(resutlt_path,str(i)+'.png'))

if __name__ == "__main__":

    file_path = os.path.join(parent_path, "python.jpg")
    image = Image.open(file_path)
    image = fill_image(image)
    image_list=cut_image(image)
    save_image(image_list)
