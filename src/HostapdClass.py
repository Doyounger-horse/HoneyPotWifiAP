from src.ExecCommandClass import ExecCommandClass
class HostapdClass:

    def __init__(self, wirelessInterface, ssid, chanel):
        self.wirelessInterface = wirelessInterface
        self.ssid = ssid
        self.chanel = chanel
        self.filenameconf = "/etc/hostapd/hostapd.conf"
        self.command = ExecCommandClass("Hostapd")

    def makeHostapdConfig(self):
        file = open(self.filenameconf,"w")
        file.write("# interface wlan du Wi-Fi\n")
        file.write("interface="+str(self.wirelessInterface)+"\n")
        file.write("# nl80211 avec tous les drivers Linux mac80211\n")
        file.write("driver=nl80211"+"\n")
        file.write("# country"+"\n")
        file.write("country_code=FR"+"\n")
        file.write("# iso 80211d"+"\n")
        file.write("ieee80211d=1"+"\n")
        file.write("# logger"+"\n")
        file.write("logger_syslog=-1"+"\n")
        file.write("logger_syslog_level=2"+"\n")
        file.write("logger_stdout=-1"+"\n")
        file.write("logger_stdout_level=2"+"\n")
        file.write("#dump"+"\n")
        file.write("dump_file=/tmp/hostapd.dump"+"\n")
        file.write("# ctrl interface"+"\n")
        file.write("ctrl_interface=/var/run/hostapd"+"\n")
        file.write("ctrl_interface_group=0"+"\n")
        file.write("# Nom du spot Wi-Fi\n")
        file.write("ssid="+str(self.ssid)+"\n")
        file.write("# mode Wi-Fi (a = IEEE 802.11a, b = IEEE 802.11b, g = IEEE 802.11g)\n")
        file.write("hw_mode=g"+"\n")     
        file.write("# canal de frequence Wi-Fi (1-14)\n")
        file.write("channel="+str(self.chanel)+"\n")
        file.write("# Wme !\n")
        file.write("wme_enabled=0"+"\n")
        file.write("# Mac acl !\n")
        file.write("macaddr_acl=0"+"\n")
        file.write("# Wi-Fi ouvert, pas d'authentification !\n")
        file.write("auth_algs=1"+"\n")
        file.write("# Beacon interval in kus (1.024 ms)\n")
        file.write("beacon_int=100"+"\n")
        file.write("# DTIM (delivery trafic information message)\n")
        file.write("dtim_period=2"+"\n")
        file.write("# Maximum number of stations allowed in station table\n")
        file.write("max_num_sta=255"+"\n")
        file.write("# RTS/CTS threshold; 2347 = disabled (default)\n")
        file.write("rts_threshold=2347"+"\n")
        file.write("# Fragmentation threshold; 2346 = disabled (default)\n")
        file.write("fragm_threshold=2346"+"\n")
        file.close()

    def startHostpad(self):
        self.makeHostapdConfig()
        self.command.execCommand("hostapd -dd -B "+str(self.filenameconf))