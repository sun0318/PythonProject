from pdf2image import convert_from_path
from PIL import Image


def pdf_to_long_image(pdf_path, output_image_path, dpi=150, quality=80):
    # 将PDF文件转换为图像列表
    images = convert_from_path(pdf_path, dpi=dpi)

    # 获取所有图像的宽度和高度，并计算长图的总高度
    total_height = sum(image.height for image in images)
    max_width = max(image.width for image in images)

    # 创建一个空白长图
    long_image = Image.new('RGB', (max_width, total_height))

    # 拼接每个页面的图像
    y_offset = 0
    for image in images:
        long_image.paste(image, (0, y_offset))
        y_offset += image.height

    # 保存长图
    long_image.save(output_image_path)
    print(f"Long image saved as {output_image_path}")


# 示例用法
pdf_path = '体检.pdf'  # 你的PDF文件路径
output_image_path = 'output_long_image.png'  # 长图输出路径
pdf_to_long_image(pdf_path, output_image_path)
