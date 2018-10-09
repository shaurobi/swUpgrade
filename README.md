# CE API calls  
A couple of functions I knocked up while testing against the CE API on Cisco Telepresence endpoints post 8.x
The pushUpgrade function can be used to remotely upgrade an endpoint, and was a function I wrote for a colleague that needed a way to remotely upgrade unmanaged endpoints to a sufficient version that they could register to Webex.
The resetCam function was just to ensure that I was making API calls effectively, beyond receiving a "200" response from the endpoint, I could visibly see the camera moving. I'm sure someone will find it useful for something. 

I built against 9.3, API guide below:
https://www.cisco.com/c/dam/en/us/td/docs/telepresence/endpoint/ce93/collaboration-endpoint-software-api-reference-guide-ce93.pdf
