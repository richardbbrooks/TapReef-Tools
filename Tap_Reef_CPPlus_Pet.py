import httplib
import time
import pickle

fish_id = 200000
tank_id = pickle.load(open("./tank_id.p"))
user_id = pickle.load(open("./user_id.p"))
device_id = pickle.load(open("./device_id.p"))
message_id = 968327162
count = 0

touch_fish = "/app_live_1.2/logic/touch_fish.php?fish_id=%d&tank_id=%d&user_id=%d&device_id=%s&message_id=%d"

while count < 1000:

	conn = httplib.HTTPConnection("www.tapreef.com")
	conn.request("GET", touch_fish % (fish_id, tank_id, user_id, device_id, message_id))
	r1 = conn.getresponse()
	
	fish_id += 1
	count += 1

	# PRINT HTTP ERROR/SUCCESS CODES
	# print r1.status, r1.reason

	print fish_id 
	print count
	print r1.read()

	conn.close()
	
	time.sleep(10)