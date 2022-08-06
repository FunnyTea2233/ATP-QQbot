import os
import cv2
import numpy as np
import ast
from PIL import ImageFont, Image, ImageDraw
import time
import psutil
import multiprocessing
import pynvml
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0) # 0表示显卡标号
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
mem = psutil.virtual_memory()
# 系统总计内存
zj = float(mem.total) / 1024 / 1024 / 1024
# 系统已经使用内存
ysy = float(mem.used) / 1024 / 1024 / 1024
# 系统空闲内存
kx = float(mem.free) / 1024 / 1024 / 1024

sent_before = psutil.net_io_counters().bytes_sent  # 已发送的流量
recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
time.sleep(1)
sent_now = psutil.net_io_counters().bytes_sent
recv_now = psutil.net_io_counters().bytes_recv
sent = (sent_now - sent_before)/1024  # 算出1秒后的差值
recv = (recv_now - recv_before)/1024

gpu_t = meminfo.total/1024**2
gpu_u = meminfo.used/1024**2
gpu_b = int(gpu_u/gpu_t*100)
print(gpu_b)

l1, l2, l3 = psutil.getloadavg()
CPU_use = (l3/os.cpu_count()) * 100

print(psutil.cpu_count(False))
print(multiprocessing.cpu_count())

print(psutil.cpu_percent())
print(psutil.cpu_stats())
print(psutil.cpu_freq())

def write_pic(number):
    bk_img = cv2.imread("resource/jiankong.png")
    # 设置需要显示的字体
    fontpath = "resource/minecraft.TTF"
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息
    draw.text((90, 100), 'CPU', font=ImageFont.truetype(fontpath, 52),fill=(255, 255, 255))
    draw.text((110, 250), str(int(psutil.cpu_percent())) + '%', font=font, fill=(255, 255, 255))

    draw.text((90, 450), 'GPU', font=ImageFont.truetype(fontpath, 52), fill=(255, 255, 255))
    draw.text((115, 550), str(gpu_b) + '%', font=font, fill=(255, 255, 255))

    draw.text((330, 100), 'RAM', font=ImageFont.truetype(fontpath, 52), fill=(255, 255, 255))
    draw.text((330, 250), str(int(ysy)) + '/' + str(int(zj)+1) + 'G', font=font, fill=(255, 255, 255))
    draw.text((330, 350), '————', font=font, fill=(255, 255, 255))
    draw.text((335, 450), 'Free', font=font, fill=(255, 255, 255))
    draw.text((350, 550), str(int(kx)) + ' G', font=font, fill=(255, 255, 255))

    draw.text((575, 250), 'NET', font=ImageFont.truetype(fontpath, 52), fill=(255, 255, 255))
    draw.text((530, 350), '+' + "{0}KB/s".format("%.2f"%sent), font=font, fill=(255, 255, 255))
    draw.text((530, 450), '-' + "{0}KB/s".format("%.2f"%recv), font=font, fill=(255, 255, 255))

    draw.text((575, 75), time.strftime('%m-%d \n \n %H:%M',time.localtime(time.time())), font=font, fill=(255, 255, 255))

    bk_img = np.array(img_pil)
    cv2.waitKey()
    createName = number + ".jpg"
    cv2.imwrite(createName, bk_img)


if __name__ == '__main__':
        write_pic('BB' + "_" + str(2))
