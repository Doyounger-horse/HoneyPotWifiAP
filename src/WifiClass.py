import wifi

class WifiClass:

    def __init__(self,interface):
        self.interface = interface
        self.apAvailable = self.scanWifiAvailable()
    
    def scanWifiAvailable(self):
        ap = []
        cells = wifi.Cell.all(self.interface)
        for c in cells:
            ap.append(c)
        return ap

    def searchSSID(self, ssid):
        f = []
        for c in self.apAvailable:
            if ssid in c.ssid:
                f.append(c)
        return f
    
    def getApAvailable(self):
        return self.apAvailable