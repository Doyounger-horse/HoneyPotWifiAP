from src.WifiClass import WifiClass

w = WifiClass("wlan0")
print "AVALABLE => "+str(w.getApAvailable())
print "FOUND => "+str(w.searchSSID("Free"))