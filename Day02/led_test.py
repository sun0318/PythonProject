import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def hex_to_binary(hex_string):
    decimal_value = int(hex_string, 16)
    binary_string = bin(decimal_value)[2:]
    padded_binary_string = binary_string.zfill(16)
    return padded_binary_string


def control_led(binary_string):
    leds = [int(bit) for bit in binary_string]
    return leds


# 主程序
if __name__ == "__main__":
    while True:
        hex_param = input("请输入十六进制参数: ")
        try:
            binary_param = hex_to_binary(hex_param)
            leds = control_led(binary_param)

            # 创建展示区
            fig, axes = plt.subplots()

            # 绘制左侧指示灯
            axes.add_patch(Circle((0.3, 0.5), 0.2, color='yellow' if leds[0] == 1 else 'gray'))
            axes.text(0.3, 0.5, 'LED 1', ha='center', va='center')

            # 绘制右侧指示灯
            axes.add_patch(Circle((0.7, 0.5), 0.2, color='yellow' if leds[1] == 1 else 'gray'))
            axes.text(0.7, 0.5, 'LED 2', ha='center', va='center')

            # 设置坐标轴范围和隐藏坐标轴
            axes.set_xlim(0, 1)
            axes.set_ylim(0, 1)
            axes.axis('off')

            plt.show()
        except ValueError:
            print("无效的输入，请输入有效的十六进制数值。")
