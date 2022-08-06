import os
import ast
import socket
import codecs

import botpy
from botpy import logging

from botpy.types.message import Reference
from botpy.message import Message
from botpy.ext.cog_yaml import read

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))
_log = logging.get_logger()

user_ref = {' 123': 'abc', ' 456': 'efg', ' 789': 'hij'}

class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")
    async def on_at_message_create(self, message: Message):
        user_txt = message.content.split('<')[1].split('>')[1]
        user_gjc = user_txt in user_ref
        if user_gjc == True:
            await self.api.post_message(channel_id=message.channel_id, content=user_ref[user_txt], msg_id=message.id)
        elif user_txt.split(' ')[1] == '/ping':
            sip = user_txt.split('/ping ')[1].split(':')[0]
            if sip == '':
                await self.api.post_message(channel_id=message.channel_id, content='格式：/ping 服务器IP:端口',msg_id=message.id)
            else:
                sport = user_txt.split('/ping ')[1].split(':')[1]
                server = open("server.yaml", "w")
                server.write('server_ip: ' + f'{sip}' + '\n')
                server.write('server_port: ' + sport)
                server.close()
                # await self.api.post_message(channel_id=message.channel_id,content=os.popen('python ping.py').read(),msg_id=message.id)
                os.popen('python title.py').read()
                await message.reply(file_image="BB_1.jpg")
        elif user_txt == ' /zt1 ':
            server = open("server.yaml", "w")
            server.write('server_ip: ' + 'mxscharity.tpddns.cn' + '\n')
            server.write('server_port: ' + '12300')
            server.close()
            mcping = os.popen('python ping.py').read()
            if mcping != 'False\n':
                os.popen('python title.py').read()
                await message.reply(file_image="BB_1.jpg")
            else:
                await message.reply(file_image="resource/stop.png")
        elif user_txt == ' /zt2 ':
            server = open("server.yaml", "w")
            server.write('server_ip: ' + 'mxscharity.tpddns.cn' + '\n')
            server.write('server_port: ' + '12301')
            server.close()
            mcping = os.popen('python ping.py').read()
            if mcping != 'False\n':
                os.popen('python title.py').read()
                await message.reply(file_image="BB_1.jpg")
            else:
                await message.reply(file_image="resource/stop.png")
        elif user_txt == ' /zt3 ':
            server = open("server.yaml", "w")
            server.write('server_ip: ' + 'mxscharity.tpddns.cn' + '\n')
            server.write('server_port: ' + '12302')
            server.close()
            mcping = os.popen('python ping.py').read()
            if mcping != 'False\n':
                os.popen('python title.py').read()
                await message.reply(file_image="BB_1.jpg")
            else:
                await message.reply(file_image="resource/stop.png")
        elif user_txt == ' /zt4 ':
            server = open("server.yaml", "w")
            server.write('server_ip: ' + 'mxscharity.tpddns.cn' + '\n')
            server.write('server_port: ' + '25565')
            server.close()
            mcping = os.popen('python ping.py').read()
            if mcping != 'False\n':
                os.popen('python title.py').read()
                await message.reply(file_image="BB_1.jpg")
            else:
                await message.reply(file_image="resource/stop.png")
        elif user_txt == ' /server ':
            os.popen('python jiankong.py').read()
            await message.reply(file_image="BB_2.jpg")
        elif user_txt == ' /all ':
            zt1 = ast.literal_eval(os.popen('python allserver/zt1.py').read())
            zt2 = ast.literal_eval(os.popen('python allserver/zt2.py').read())
            zt3 = ast.literal_eval(os.popen('python allserver/zt3.py').read())
            zt4 = ast.literal_eval(os.popen('python allserver/zt4.py').read())
            server_stop = '暂未开启'
            fgx = '——————————————————'
            if zt1 == False:
                zt1 = '[一服]' + server_stop + '\n' + \
                      fgx + '\n'
            else:
                zt1 = '[一服]' + test_config["zt1_txt"] + '\n' + \
                      '[版本]' + zt1[1]['version'] + '\n' + \
                      '[简介]' + zt1[1]['name'] + '\n' + \
                      '[人数]' + zt1[1]['online_players'] + '/' + zt1[1]['max_players'] + '\n' + \
                      fgx + '\n'
            if zt2 == False:
                zt2 = '[二服]' + server_stop + '\n' + \
                      fgx + '\n'
            else:
                zt2 = '[二服]' + test_config["zt2_txt"] + '\n' + \
                      '[版本]' + zt2[1]['version'] + '\n' + \
                      '[简介]' + zt2[1]['name'] + '\n' + \
                      '[人数]' + zt2[1]['online_players'] + '/' + zt2[1]['max_players'] + '\n' + \
                      fgx + '\n'
            if zt3 == False:
                zt3 = '[三服]' + server_stop + '\n' + \
                      fgx + '\n'
            else:
                zt3 = '[三服]' + test_config["zt3_txt"] + '\n' + \
                      '[版本]' + zt3[1]['version'] + '\n' + \
                      '[简介]' + zt3[1]['name'] + '\n' + \
                      '[人数]' + zt3[1]['online_players'] + '/' + zt3[1]['max_players'] + '\n' + \
                      fgx + '\n'
            if zt4 == False:
                zt4 = '[四服]' + server_stop + '\n' + \
                      fgx + '\n'
            else:
                zt4 = '[四服]' + test_config["zt4_txt"] + '\n' + \
                      '[版本]' + zt4[1]['version'] + '\n' + \
                      '[简介]' + zt4[1]['name'] + '\n' + \
                      '[人数]' + zt4[1]['online_players'] + '/' + zt4[1]['max_players'] + '\n' + \
                      fgx + '\n'


            all_txt = zt1 + zt2 + zt3 + zt4 + 'ATPBot BY-FunnyTea'
            await self.api.post_message(channel_id=message.channel_id,content=all_txt,msg_id=message.id)
        elif user_txt == ' /mojang ':
            os.popen('python title.py').read()
            await self.api.post_message(channel_id=message.channel_id, content='开发中', msg_id=message.id)
        else:
            await self.api.post_message(channel_id=message.channel_id, content='?', msg_id=message.id)


if __name__ == "__main__":
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])
