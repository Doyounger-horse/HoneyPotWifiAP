import subprocess
from src.MonitoringClass import MonitoringClass

class MakeAPClass:
    
    def __init__(self, essid, chanel, interface, interfacemon):
        self.essid = essid
        self.chanel = chanel
        self.interface = interface
        self.interfacemon = interfacemon
        self.fileconfname = "/etc/hostapd/hostapd.conf"

    def makeAP(self):
        try:
            command = "hostapd "+self.fileconfname
            proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output,error = proc.communicate()
            if output:
                print output
            if error:
                print error
        except KeyboardInterrupt:
            print "Interrupt"
            exit()
        except:
            print "Error AP"
            exit()

    
