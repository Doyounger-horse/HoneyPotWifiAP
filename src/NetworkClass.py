import subprocess
from src.ExecCommandClass import ExecCommandClass
class NetworkClass:

    def __init__(self, wint):
        self.wint = wint
        self.command = ExecCommandClass("Test")

    def stopNM(self):
        self.command.execCommand("service network-manager stop")

    def stopDnsMasq(self):
        self.command.execCommand("service dnsmasq stop")

    def stopWint(self):
        self.command.execCommand("ifconfig "+str(self.wint)+" down")

    def startWint(self):
        self.command.execCommand("ifconfig "+str(self.wint)+" up")