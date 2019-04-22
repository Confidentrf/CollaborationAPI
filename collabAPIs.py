#!/usr/bin/env python
#title           :collabAPICalls.py
#description     :This will create a header for a python script.
#author          :Richard Ferguson
#date            :02.26.2019
#version         :1.0
#usage           :python collabAPIs.py
#notes           : REST API for Collaboration Management and ease of useage for collaboration Endpoints
#                  If there are any question regarding useage and lines of code please contact 
#				   this scripts architect. 
#python_version  :3.6.5
#==============================================================================

import json
import requests
import time
import xmltodict
import collabCfg
import paramiko
import config
from paramiko import client
from lxml import etree
#from codec.templates import survey, register, last, dial
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests import get, post
from KalturaClient import *
from KalturaClient.Plugins.Core import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CatturaCapture:
	def __init__(self, urlAPI={},auth_values={}, userInput={} ,caturaSSHAuth={}):
		print ('Enter Unit IP')
		self.urlAPI = urlAPI
		self.userInput = input()
		self.urlAPIs = "http://"+self.userInput+"/api/1/"
		self.auth_values = (collabCfg.cattura['user'], collabCfg.cattura['passwd'])
		self.caturaSSHAuth = (collabCfg.cattura['userSSh'],collabCfg.cattura['keySSh'])

		

	def statusCheck(self):
		url = self.urlAPIs
		statusUrl = url+"status"
		auth = self.auth_values
		#urlStatus = "http://"+input()+"/api/1/status?since"
		#auth_values = (collabCfg.cattura['user'], collabCfg.cattura['passwd'])
		box = requests.get(statusUrl, auth=auth)
		print (box.json())	

	def guiReboot(self):
		url = self.urlAPIs	
		auth = self.auth_values	
		creboot = url+"maintenance/reboot"
		box = requests.post(creboot, auth=auth)
		if box:
			print ('Connected, Performing Operation!')
			print (box.json())
		else:
			print ('Unable to connect!')

	def sshReboot(self):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.userInput, port=22, username=collabCfg.cattura['userSSh'], password=collabCfg.cattura['keySSh'] )
		'''
		if connect:
			print('Login Successful')
		else:
			print('Unable to login, please check to see if the box is on or check your credentials...')
		'''
		stdin, stdout, stderr = ssh.exec_command('reboot -f', get_pty = True)
		time.sleep(2)
		stdin, stdout, stderr = ssh.exec_command(collabCfg.cattura['keySSh'])
		
		output = stdout.readlines()
		type(output)
		print ('\n'.join(output))

	def startRec(self):
		url = self.urlAPIs 
		auth = self.auth_values
		startRec = url+"capture/start"

		data={ "title": "RCF_Script test one",				
				"duration": 36000000,
						"tags": ["RCF_Scriptin"],
						"templateID": "Default_template",
						"options": { },
						"metadata": { },
						"publishingOverrides": {

								"kaltura": {
								"ownerID": "bob@example.com"
							}
						},		
						"speaker": "Almighty Bob",
						"publishing": "true",
						"publishingRedundantCopies": "true",
						"publishingSpeakerFiles": "true",
						"publishingSpeakerInformation": "true",
						"publishingTableOfContents": "true" 
						}
		json_data = (json.dumps(data))
		headers = {'content-type':'application/x-www-form-urlencoded'}
		payload={"captureRequest": json_data}
		requests.post(startRec.format(), data=payload, auth=auth)
"""
		if :
			print ('Starting Capture')
		else:
			print ('Failed to start capture!')
"""
	
class telepresenceEps:
	def __init__(self, xapi={}, auth_values={}, userInput={}):
		print ('Enter Unit IP')
		self.xapi = xapi
		self.userInput = input()
		self.auth_values=(collabCfg.cisco['user'],collabCfg.cisco['remote'])
		self.xapi = 'https://'+self.userInput+'/getxml?location=/Status/Standby'
		#epCon = requests.get(self.xapi, auth=auth)
		

	def get_status(self):
		auth = self.auth_values
		url = self.xapi
		response  = requests.get(url, verify=False, timeout=2, auth=auth)
		xmlstr = response.content
		root = etree.fromstring(xmlstr)
		status = root.xpath('//Status/SystemUnit/te/text()')[0]

		if status:
			print("Connected To endpoint")
		else:
			print("No Connection was established.")
		print(status)

telepresenceEps().get_status()

"""
class KalturaVMS:
	def __init__(self, kalturaApi={},auth_values={}, kConfig = {}, clientDesc = {}, kclient = {}, kUserID = {}, ktype = {}, pID = {}, kprivalages = {} ):
		self.kalturaApi = kalturaApi
		self.kalturaApis= (collabCfg.kaltura['url'])
		self.kclient = (collabCfg.kaltura['client'])
		self.clientDesc = (collabCfg.kaltura['clientDesc'])
		self.kUserID = (collabCfg.kaltura['user'])
		self.ktype = (collabCfg.kaltura['k_type'])
		self.pID = (collabCfg.kaltura['partner_id'])
		self.kprivalages = (collabCfg.kaltura['privileges'])
		self.expire = (collabCfg.kaltura['expiry'])
		auth = (self.kclient, self.kUserID, self.ktype, self.pID, self.expire, self.kprivalages)
		ks = collabCfg.kaltura['clientDesc']session.start(auth)

		if ks:
			print('Connected!')

		else:
			print("Not Connected \n")
	def filture(self):
		
		time.sleep(3)
		
		if connect:
			print("Connection Established!")
		else: 
			print("Not connected Check your syntax \n")
"""