import os
import platform
import http.client
#function to push upgrades to endpoints that are reachable by L3
def pushUpgrade(clientIp, serverIp):
	conn = http.client.HTTPConnection(clientIp)
	payload = "<Command>\n\t<SystemUnit>\n\t\t<SoftwareUpgrade>\n\t\t\t<URL>\"http://"+serverIp+"/s52030ce8_3_4.pkg\"</URL>\n\t\t</SoftwareUpgrade>\n\t</SystemUnit>\n</Command>"
	headers = {
	    'content-type': "text/xml",
	    'cache-control': "no-cache",
	    'postman-token': "23123b44-02ee-ee90-eb2d-146256e97fc8"
	    }

	conn.request("POST", "/putxml", payload, headers)
	res = conn.getresponse()
	data = res.read()
	print(data.decode("utf-8"))

#function to ping the machine to test connectivity.
def ping(address):
	giveFeedback = False
	if platform.system()== "Windows":
		response = os.system("ping "+address+" -n 1")
	else:
		response = os.system("ping -c 1 " +address)
		
	if response == 0:
		return True
	else:
		return False

#function to test API connectivity by moving the camera
def resetCam(address):
	conn = http.client.HTTPConnection(address)

	payload = "<Command>\n\t<Camera>\n\t\t<PositionReset>\n\t\t\t<CameraId>1</CameraId>\n\t\t</PositionReset>\n\t</Camera>\n</Command>"

	headers = {
	    'content-type': "text/xml",
	    'authorization': "Basic YWRtaW46",
	    'cache-control': "no-cache",
	    'postman-token': "1ba2946a-79fb-4810-ee8f-b9da63dc4f80"
	    }

	conn.request("POST", "/putxml", payload, headers)

	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8"))

#test address for local codec
testaddy = "192.168.1.52"


address = input("Please enter the IP Address of the endpoint in the format x.x.x.x:\n")
if address == 0:
	address = testaddy
if ping(address) == True:
	print("Address is reachable")
else:
	print("Address is unreachable, please check address and try again")
	exit()

