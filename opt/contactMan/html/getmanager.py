#!/usr/bin/python

import json
import urllib2
import MySQLdb

def skipalevel(manid):
	sneconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
	snecur = sneconn.cursor()
	strtjr = urllib2.urlopen('http://org-dir.nm.4x3i.com:38700/employeeData/'+str(manid))
	getter = strtjr.read()
	myj = json.loads(getter)
	empid = myj['empId'].encode('ascii', 'ignore')
	name = myj['name'].encode('ascii', 'ignore')
	email = myj['email'].encode('ascii', 'ignore')
	phone = myj['mobile'].encode('ascii', 'ignore')
	hisman = myj['manager'].encode('ascii', 'ignore')
	team = myj['functionName'].encode('ascii', 'ignore')
	manid = myj['managerId'].encode('ascii', 'ignore')
	checkman = "select empid from contactman where empid='%s'" %(empid)
	snecur.execute(checkman)
	dat = snecur.fetchall()
	if len(dat) == 0:
		quer = 'insert into contactman(empid, name, email_id, phnum, team, manager, manid, updated_date) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", current_timestamp())' %(empid, name, email, phone, team, hisman, manid)
		snecur.execute(quer)
		sneconn.commit()
	else:
		pass
	sneconn.close()

def sneaker(empid):
	sneconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
	snecur = sneconn.cursor()
	strtjr = urllib2.urlopen('http://org-dir.nm.4x3i.com:38700/employeeData/'+str(empid))
	getter = strtjr.read()
	myj = json.loads(getter)
	empid = myj['empId'].encode('ascii', 'ignore')
	name = myj['name'].encode('ascii', 'ignore')
	email = myj['email'].encode('ascii', 'ignore')
	phone = myj['mobile'].encode('ascii', 'ignore')
	hisman = myj['manager'].encode('ascii', 'ignore')
	team = myj['functionName'].encode('ascii', 'ignore')
	manid = myj['managerId'].encode('ascii', 'ignore')
	skipalevel(myj['managerId'].encode('ascii', 'ignore'))
	checkman = "select empid from contactman where empid='%s'" %(empid)
	snecur.execute(checkman)
	dat = snecur.fetchall()
	if len(dat) == 0:
		quer = 'insert into contactman(empid, name, email_id, phnum, team, manager, manid, updated_date) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", current_timestamp())' %(empid, name, email, phone, team, hisman, manid)
		snecur.execute(quer)
		sneconn.commit()
	else:
		pass
	sneconn.close()

if __name__ == "__main__":
	print "this app will not run directly"
