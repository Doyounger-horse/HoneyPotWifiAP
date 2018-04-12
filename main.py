# from src.WifiClass import WifiClass
# w = WifiClass("wlan0")
# print "AVALABLE => "+str(w.getApAvailable())
# print "FOUND => "+str(w.searchSSID("toto"))

from src.DnsMasqClass import DnsMasqClass
from src.HostapdClass import HostapdClass
from src.IptablesClass import IptablesClass
from src.NetworkClass import NetworkClass

internetInterface = raw_input("Interface with internet (eth0) > ")
wirelessInterface = raw_input("Wireless Interface (wlan0) > ")
ssid = raw_input("SSID > ")
chanel = raw_input("Chanel > ")

dns = DnsMasqClass(wirelessInterface,"192.168.1.150","192.168.1.200","1.1.1.1")
hapd = HostapdClass(wirelessInterface,ssid,chanel) 
ipta = IptablesClass(internetInterface)
netw = NetworkClass(wirelessInterface)


print '\033[93m'+"Stopping NM"+'\033[0m'
netw.stopNM()
print '\033[92m'+"Stoped"+'\033[0m'
print '\033[93m'+"Stopping Dnsmasq"+'\033[0m'
dns.stopDnsMasq()
print '\033[92m'+"Stoped"+'\033[0m'
print '\033[93m'+"Down Winf"+'\033[0m'
netw.stopWint()
print '\033[92m'+"Stoped"+'\033[0m'
print '\033[93m'+"Start hostapd"+'\033[0m'
hapd.startHostpad()
print '\033[92m'+"Started"+'\033[0m'
print '\033[93m'+"Start winf"+'\033[0m'
netw.startWint()
print '\033[92m'+"Started"+'\033[0m'
print '\033[93m'+"Start dnsmasq"+'\033[0m'
dns.startDnsMasq()
print '\033[92m'+"Started"+'\033[0m'
print '\033[93m'+"Config Iptables"+'\033[0m'
ipta.setupIptables()
print '\033[92m'+"Configured"+'\033[0m'
print '\033[95m'+"AP ALIVE"+'\033[0m'


