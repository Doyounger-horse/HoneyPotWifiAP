import subprocess

class ExecCommandClass:

    def __init__(self, name):
        self.name = name

    def execCommand(self, command):
        try:
            proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output,error = proc.communicate()
            if output:
                print '\033[92m'+"OUT > "+'\033[0m'+output
            if error:
                print '\033[91m'+"ERR > "+'\033[0m'+error
        except KeyboardInterrupt:
            print '\033[93m'+"Interrupt "+str(self.name)+'\033[0m'
            exit()
        except:
            print '\033[93m'+"Error "+str(self.name)+'\033[0m'
            exit()