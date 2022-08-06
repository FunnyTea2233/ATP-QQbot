import os
import cv2
import numpy as np
import ast
from PIL import ImageFont, Image, ImageDraw

def write_pic(number):
    players_list = os.popen('python players.py').read()
    players = ast.literal_eval(players_list)
    mcping = os.popen('python ping.py').read()
    mcname = ast.literal_eval(mcping)

    bk_img = cv2.imread("resource/server3.png")
    # 设置需要显示的字体
    fontpath = "resource/minecraft.TTF"
    font = ImageFont.truetype(fontpath, 32)
    img_pil = Image.fromarray(bk_img)
    draw = ImageDraw.Draw(img_pil)
    # 绘制文字信息
    draw.text((280, 30), mcname[1]['name'], font=font, fill=(238,252,8))
    draw.text((660, 140), 'Version: ' + mcname[1]['version'], font=font, fill=(238, 252, 8))
    draw.text((660, 180), 'Players: ' + mcname[1]['online_players'] + '/' + mcname[1]['max_players'], font=font, fill=(238, 252, 8))

    for i in range(len(players)):
        if i <= 5:
            draw.text((30, 300 + i * 130), players[i], font=font, fill=(255, 255, 255))
        if i > 5:
            j = 6
            k = i - j
            draw.text((400, 300 + k * 130), players[i], font=font, fill=(255, 255, 255))
        if i > 11:
            j = 12
            k = i - j
            draw.text((800, 300 + k * 130), players[i], font=font, fill=(255, 255, 255))



    bk_img = np.array(img_pil)
    cv2.waitKey()
    createName = number + ".jpg"
    cv2.imwrite(createName, bk_img)


if __name__ == '__main__':
    for i in range(1, 2):
        write_pic('BB' + "_" + str(i))
