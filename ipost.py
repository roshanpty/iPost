#!/usr/bin/env python3

import requests
import json

def getSessionID():
	sessionid = "SESSIONID"
	return sessionid

def checkValidLogin(sid):
	# Send a request to own profile
	# If there is a set cookie header for sessionid in response, it is not a valid session
	authstatus = "AUTHSTATUS"
	return authstatus

def getLoginForm():
	csrftoken = "CSRFTOKEN"
	return csrftoken

def sendLoginRequest():
	sessionid = "SESSIONID"
	return sessionid

def fileUpload():
	uploadstatus = "UPLOADED"
	return uploadstatus

def getCSRFToken();
	csrftoken = "CSRFTOKEN"
	return csrftoken


sid = getSessionID()
aStat = checkValidLogin(sid)
if aStat == True:
	csrf = getCSRFToken()
	fileUpload(file)
else:
	csrf = getLoginForm()
	sid = sendLoginRequest()
	csrf = getCSRFToken()
	fileUpload(file)

