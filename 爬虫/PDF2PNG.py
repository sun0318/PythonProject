from pdf2image import convert_from_path


def pdf_to_images(pdf_path, output_folder, dpi=300):
    # 将PDF文件转换为图像
    images = convert_from_path(pdf_path, dpi=dpi)
    print(images)

    # 保存图像到指定文件夹
    for i, image in enumerate(images):
        output_path = f"{output_folder}/page_{i + 1}.png"
        # image.save(output_path, 'PNG')
        print(f"Page {i + 1} saved as {output_path}")


# 示例用法
pdf_path = "体检.pdf"  # 你的PDF文件路径
output_folder = 'output_images'  # 图像输出文件夹
pdf_to_images(pdf_path, output_folder)
