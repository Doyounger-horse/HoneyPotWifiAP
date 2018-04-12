from src.ExecCommandClass import ExecCommandClass
class IptablesClass:

    def __init__(self, internetInterface):
        self.internetInterface = internetInterface
        self.command = ExecCommandClass("Iptables")

    def setupIptables(self):
       self.command.execCommand("iptables -F") 
       self.command.execCommand("iptables -X") 
       self.command.execCommand("iptables -t nat -F") 
       self.command.execCommand("iptables -t nat -X") 
       self.command.execCommand("iptables -P INPUT ACCEPT") 
       self.command.execCommand("iptables -P FORWARD ACCEPT") 
       self.command.execCommand("iptables -P OUTPUT ACCEPT")
       self.command.execCommand("iptables -t nat -A POSTROUTING -o "+self.internetInterface+" -j MASQUERADE")
       self.command.execCommand("echo 1 > /proc/sys/net/ipv4/ip_forward")