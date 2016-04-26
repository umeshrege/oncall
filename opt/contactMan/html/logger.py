#!/usr/bin/python

import datetime

def login(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
	go = str(now)+" "+str(uname)+" logged in\n"
	logger.write(str(go))
	logger.close()

def register(uname, addi=""):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
	go = str(now)+" "+str(uname)+" has been registered" + " " + str(addi) + "\n"
	logger.write(str(go))
	logger.close()

def phone(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
        go = str(now) + " " + str(uname) + " updated phonenumber\n"
        logger.write(go)
        logger.close()

def primoncall(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
        go = str(now) + " " + str(uname) + " updated to primary On-call\n"
        logger.write(go)
        logger.close()

def seconcall(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
        go = str(now) + " "+ str(uname) + " updated to secondary on-call\n"
        logger.write(go)
        logger.close()

def team(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
        go = str(now) + " " + str(uname) + " updated the teamname\n"
        logger.write(go)
        logger.close()

def Delteam(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
        go = str(now) + " " + str(uname) + " has been removed from the table team\n"
        logger.write(go)
        logger.close()

def logout(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
        go = str(now) + " "+ str(uname) + " has logged out\n"
        logger.write(go)
        logger.close()

def incorrect(uname):
	logger = open('/opt/contactMan/logs/yp.log', 'a')
	now = datetime.datetime.now()
        go = str(now) + " Error: "+ str(uname) + " is possibly incorrect username or the username-password combination is incorrect\n"
        logger.write(go)
        logger.close()
