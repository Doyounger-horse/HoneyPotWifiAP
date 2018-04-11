import subprocess

class MakeAPClass:
    
    def __init__(self, mac, essid, chanel, interface):
        self.mac = mac
        self.essid = essid
        self.chanel = chanel
        self.interface = interface
        self.fileconfname = "/etc/hostapd/hostapd.conf"

    def makeAP(self):
        try:
            command = "hostapd "+self.fileconfname
            proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            out,err = proc.communicate()
            print out
            print err
        except KeyboardInterrupt:
            print "Interrupt"
            exit()
        except:
            print "Error AP"

    def makeHostapdConfig(self):
        file = open(self.fileconfname,"w")
        file.write("# interface wlan du Wi-Fi\n")
        file.write("interface="+str(self.interface)+"\n")
        file.write("# nl80211 avec tous les drivers Linux mac80211\n")
        file.write("driver=nl80211"+"\n")
        file.write("# Nom du spot Wi-Fi\n")
        file.write("ssid="+str(self.essid)+"\n")
        file.write("# mode Wi-Fi (a = IEEE 802.11a, b = IEEE 802.11b, g = IEEE 802.11g)\n")
        file.write("hw_mode=g"+"\n")     
        file.write("# canal de frequence Wi-Fi (1-14)\n")
        file.write("channel="+str(self.chanel)+"\n")
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
