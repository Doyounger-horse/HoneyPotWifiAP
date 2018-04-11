import subprocess

class MonitoringClass:

    def __init__(self, interface):
        self.interface = interface

    
    def setMonitor(self):
        bashCommand = "sudo airmon-ng start {}".format(self.interface)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output
        print error
