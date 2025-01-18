from PIL import Image
import os


def check_image_requirements(img):
    width, height = img.size
    if width < 192 or height < 144:
        raise ValueError("图像分辨率不满足最低要求：192x144像素")


def compress_image(input_path, output_path, min_size_kb=20, max_size_kb=200):
    # 打开图像
    img = Image.open(input_path)

    # 检查图像是否符合要求
    check_image_requirements(img)

    # 初始质量
    quality = 95

    # 二分法压缩图像
    while True:
        # 保存图像到内存
        with open(output_path, 'wb') as out:
            img.save(out, format='JPEG', quality=quality)

        # 获取文件大小
        file_size_kb = os.path.getsize(output_path) / 1024

        # 检查文件大小是否符合要求
        if min_size_kb <= file_size_kb <= max_size_kb or quality <= 5:
            break

        # 调整质量，继续压缩
        quality -= 5 if file_size_kb > max_size_kb else -5

    print(f"图像已压缩到 {file_size_kb:.2f} KB，质量为 {quality}")


# 示例用法
input_path = '照片.jpg'
output_path = 'output1.jpg'
compress_image(input_path, output_path, min_size_kb=20, max_size_kb=150)
