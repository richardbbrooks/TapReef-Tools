import httplib
import plistlib

conn = httplib.HTTPConnection("www.tapreef.com")
conn.request("GET", "/app_live_1.2/store/available_store_items.php")
resp = conn.getresponse()
plist = plistlib.readPlistFromString(resp.read())
fish_plist = plist["FISH"]

for i in range(len(fish_plist)-1):
	print fish_plist[i]["name"] + "\t" + fish_plist[i]["sellvalue"] + "\t" + fish_plist[i]["hardiness"]

conn.close()