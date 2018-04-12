import subprocess
from src.ExecCommandClass import ExecCommandClass
class NetworkClass:

    def __init__(self, wirelessInterface):
        self.wirelessInterface = wirelessInterface
        self.command = ExecCommandClass("Test")

    def stopNM(self):
        self.command.execCommand("service network-manager stop")

    def stopDnsMasq(self):
        self.command.execCommand("service dnsmasq stop")

    def stopWint(self):
        self.command.execCommand("ifconfig "+str(self.wirelessInterface)+" down")

    def startWint(self):
        self.command.execCommand("ifconfig "+str(self.wirelessInterface)+" up")