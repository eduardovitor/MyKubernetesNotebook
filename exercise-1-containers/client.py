import os
import requests


# Get server address from env. If not specified, use
# "localhost" as default value.
server = os.environ.get("SERVER_ADDRESS", "http://localhost")
# Get server port from env. If not specified, use
# "5001"  as default value.
port = int(os.environ.get("SERVER_PORT", 5001))

# Get user ID of the request. 
# If not specified, use 1 as default value.
userID = int(os.environ.get("USER_ID", 1))
# Make a request!
r = requests.get("%s:%d/user/%d/firstname" % (server, port, userID))

if r.status_code == 200: 
    print("got response: ", r.json())
    print("DONE!!!! :-)")
else:
    print(r.text)
