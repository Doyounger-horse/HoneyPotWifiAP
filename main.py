from src.WifiClass import WifiClass

w = WifiClass("wlan0")
print w.getApAvailable()
print w.serachSSID("eduroam")