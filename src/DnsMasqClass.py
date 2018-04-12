from src.ExecCommandClass import ExecCommandClass
class DnsMasqClass:

    def __init__(self, interface, dhcp_min, dhcp_max, dns):
        self.interface = interface
        self.dhcp_min = dhcp_min
        self.dhcp_max = dhcp_max
        self.dns = dns
        self.fileconfname = "/etc/dnsmasq.conf"
        self.command = ExecCommandClass("Dnsmasq")
    
    def makeDnsMasqConfig(self):
        file = open(self.fileconfname,"w")
        file.write("# disables dnsmasq reading any other files like /etc/resolv.conf for nameservers\n")
        file.write("no-resolv"+"\n")
        file.write("# Interface to bind to\n")
        file.write("interface="+str(self.interface)+"\n")
        file.write("# Specify starting_range,end_range,lease_time\n")
        file.write("dhcp-range="+self.dhcp_min+","+self.dhcp_max+",1h"+"\n")
        file.write("# dns addresses to send to the clients\n")
        file.write("server="+self.dns+"\n")
        file.close()

    def startDnsMasq(self):
        self.command.execCommand("dnsmasq")
