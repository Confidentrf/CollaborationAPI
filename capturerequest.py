import requests
import json

#JSON Object (Should not be hardcoded, only for example purposes)
data={ "title": "My Lecture Capture",
    "duration": 36000000,
    "tags": ["Chemistry 101"],
    "templateID": "1-src",
    "options": { },
    "metadata": { },
    "publishingOverrides": {},
    "speaker": "Almighty Bob",
    "publishing": "true",
    "publishingRedundantCopies": "true",
    "publishingSpeakerFiles": "true",
    "publishingSpeakerInformation": "true",
    "publishingTableOfContents": "true" 
    }

json_data = json.dumps(data)

# Set up URL for making the API request
reqUrl="http://10.60.53.139/api/1/capture/start"

payload={"captureRequest": json_data}
requests.post(reqUrl,data=payload)

class telepresenceEps:
    def __init__(self,xapi={}, auth_values={},userInput{}):
        print ('Enter Unit IP')
        self.xapi = xapi
        self.userInput = input()
        self.auth_values=(collabCfg.cisco[''])

        self.xapi = "ssh://"+self.userInput
        epCon = reqiuest.get(self.xapi, )

