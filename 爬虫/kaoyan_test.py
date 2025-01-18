from pdf2docx import Converter


def pdf_to_word(pdf_file_path, word_file_path, start_page=0, end_page=None):
    # 创建一个Converter对象
    cv = Converter(pdf_file_path)

    # 执行转换
    cv.convert(word_file_path, start=start_page, end=end_page)

    # 关闭Converter对象
    cv.close()


# 示例：将PDF文件转换为Word文件
pdf_file_path = "《全国大学英语四、六级考试大纲（2016年修订版）》.pdf"
word_file_path = "全国大学英语四六级考试大纲.docx"

pdf_to_word(pdf_file_path, word_file_path, start_page=16, end_page=150)

print(f"PDF文件已成功转换为Word文件，保存路径为: {word_file_path}")
