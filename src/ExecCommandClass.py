import subprocess

class ExecCommandClass:

    def __init__(self, name):
        self.name = name
        self.logFile = "./../LOG.txt"

    def execCommand(self, command):
        f=open(self.logFile,"a")
        try:
            proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output,error = proc.communicate()
            if output:
                print '\033[92m'+"OUT > "+'\033[0m'+output
                f.write("OUT > "+str(output)+"\n")
            if error:
                print '\033[91m'+"ERR > "+'\033[0m'+error
                f.write("ERR > "+str(error)+"\n")
        except KeyboardInterrupt:
            print '\033[93m'+"Interrupt "+str(self.name)+'\033[0m'
            exit()
        except:
            print '\033[93m'+"Error "+str(self.name)+'\033[0m'
            exit()
        f.close()