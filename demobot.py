import os

import socket
import codecs

import botpy
from botpy import logging

from botpy.types.message import Reference
from botpy.message import Message
from botpy.ext.cog_yaml import read

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))
_log = logging.get_logger()
mcping = os.popen('python ping.py').read()
class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_at_message_create(self, message: Message):
        # 构造消息发送请求数据对象
        message_reference = Reference(message_id=message.id)
        # 通过api发送回复消息
        content=f"机器人{self.robot.name}收到你的@消息了: {message.content}"
        await self.api.post_message(channel_id=message.channel_id, content=content,msg_id=message.id)
        # await self.api.post_message(channel_id=message.channel_id,content=os.popen('python ping.py').read(),msg_id=message.id)
        # await message.reply(file_image="resource/server4.png")
        #await message.reply(file_image="BB_1.jpg")
        # payload = {
        #          "template_id": 34,
        #          "kv": [
        #              {"key": "#PROMPT#", "value": "123"},
        #              {"key": "#METATITLE#", "value": "通知提醒"},
        #              {"key": "#METASUBTITLE#", "value": mcping},
        #              # {"key": "#METACOVER#", "value": "https://vfiles.gtimg.cn/vupload/20211029/bf0ed01635493790634.jpg"},
        #              # {"key": "#METAURL#", "value": "https://www.mcbbs.net/home.php?mod=space&uid=3281407"},
        #          ],
        #      }
        # await message.reply(ark=payload)

        # embed = {
        #     "title": "embed消息",
        #     "prompt": "消息透传显示",
        #     "fields": [
        #         {"name": "<@!1234>hello world"},
        #         {"name": "<@!1234>hello world"},
        #     ],
        # }
        # await self.api.post_message(channel_id=message.channel_id, embed=embed)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_guild_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])
