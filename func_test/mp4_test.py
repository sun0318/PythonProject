import sys
from moviepy.editor import *
video = VideoFileClip("golden-dark.mp4")
duration = video.duration # 获取视频时长（单位：秒）
width = video.size[0]    # 获取视频宽度（像素）
height = video.size[1]   # 获取视频高度（像素）
fps = video.fps          # 获取视频帧率（每秒显示多少张图片）
print(duration)

data = os.walk("/Users/wupeiqi/Documents/视频教程/路飞Python/mp4")
for path, folder_list, file_list in data:
    for file_name in file_list:
        file_abs_path = os.path.join(path, file_name)
        ext = file_abs_path.rsplit(".",1)[-1]
        if ext == "mp4":
            print(file_abs_path)
# audio = video.audio
# audio.write_audiofile("output_audio.wav", codec="pcm_s16le")