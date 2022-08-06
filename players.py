import requests
import ast
import os
from botpy.ext.cog_yaml import read

# url = 'https://api.miri.site/mcPlayer/get.php?ip=s3.kentcraft.cn&port=12302'
test_config = read(os.path.join(os.path.dirname(__file__), "server.yaml"))
url = 'https://api.miri.site/mcPlayer/get.php?ip=%s'%(test_config["server_ip"])+'&port=%d'%(test_config["server_port"])
response = requests.get(url)
players = ast.literal_eval(response.text)
# print(response.text)
# players_list = players['sample']
# print(list(players_list))
# print(players['online'])
# print(players['sample'][0]['name'])
online = len(players['sample'])
list_players = []
for i in range(online):
    list_players.append(players['sample'][i]['name'])
print(list_players)
