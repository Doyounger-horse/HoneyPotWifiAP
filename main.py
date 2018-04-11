# from src.WifiClass import WifiClass
# w = WifiClass("wlan0")
# print "AVALABLE => "+str(w.getApAvailable())
# print "FOUND => "+str(w.searchSSID("toto"))

from src.MakeAPClass import MakeAPClass

ap = MakeAPClass("22:a3:aa:a0:ba:42", "TEST", 2, "wlan0mon")
ap.makeHostapdConfig()