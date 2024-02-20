from PIL import Image, ImageFilter
def change_dpi():
    new_image_name = "resized_image.png"
    image = Image.open("ikun.png")
    # 调整分辨率
    resized_image = image.resize((90, 120))

    # 保存调整后的图像
    resized_image.save(new_image_name)
    return new_image_name