from PIL import Image
import os

def crop_center_405x405(input_path, output_path):
    # 打开图片
    with Image.open(input_path) as img:
        width, height = img.size

        # 计算中心裁剪区域
        left = (width - 642) / 2
        top = (height - 642) / 2
        right = left + 642
        bottom = top + 642

        # 执行裁剪
        cropped_img = img.crop((left, top, right, bottom))

        # 保存为 JPG
        cropped_img.save(output_path, format='JPEG')
        print(f"Image saved to: {output_path}")

# 示例用法（请替换为你自己的路径）
input_image = "/mnt/ssd/jingyi/Info/Jingyi-Official.github.io/images/Jingyi.jpg"
output_image = "/mnt/ssd/jingyi/Info/Jingyi-Official.github.io/images/Jingyi_2.jpg"

crop_center_405x405(input_image, output_image)