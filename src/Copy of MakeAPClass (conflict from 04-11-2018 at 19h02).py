import subprocess

class MakeAPClass:
    
    def __init__(self, mac, essid, chanel, interface):
        self.mac = mac
        self.essid = essid
        self.chanel = chanel
        self.interface = interface

    def makeAP(self):
        try:
            command = "airbase-ng -a "+str(self.mac)+" --essid "+str(self.essid)+" -c "+str(self.chanel)+" "+str(self.interface)
            proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            out,err = proc.communicate()
            print out
            print err
        except KeyboardInterrupt:
            print "Interrupt"
            exit()
        except:
            print "Error Ap"
