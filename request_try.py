# import pkg_resources
# pkg_resources.require("requests==2.2.0")
import requests
import sys
print(sys.version)
r = requests.get('http://localhost:3000/accessToGym/BFdTHyKXNX4lMTmOQDbw')
a = r.text
print(a)
