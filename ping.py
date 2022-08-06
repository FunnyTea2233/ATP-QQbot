import socket
import codecs
import os
from botpy.ext.cog_yaml import read
# import atpbot

class mcstatus:
    def __init__(self, hostname, port, timeout=0.6):
        self.hostname = hostname
        self.timeout = timeout
        self.port = port

    def getserverinfo(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(self.hostname)
        try:
            s.settimeout(self.timeout)
            s.connect((ip, self.port))
            s.send(bytearray([0xFE, 0x01]))
            data_raw = s.recv(1024)
            s.close()
            data = data_raw.decode('cp437').split('\x00\x00\x00')
            info = {}
            info['version'] = data[2].replace("\x00", "")
            info['name'] = data[3].replace("\x00", "")
            info['online_players'] = data[4].replace("\x00", "")
            info['max_players'] = data[5].replace("\x00", "")
            return True, info
        except socket.error:
            return False


if __name__ == '__main__':
    test_config = read(os.path.join(os.path.dirname(__file__), "server.yaml"))
    app = mcstatus(test_config["server_ip"], test_config["server_port"])
    # app = mcstatus(atpbot.sip, atpbot.sport)

print(app.getserverinfo())
# pi = app.getserverinfo()
# print(pi[0])
# print(pi[1].get('version'))