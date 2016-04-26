#!/usr/bin/python

import MySQLdb
import json
import cgi

dat = cgi.FieldStorage()
empid = dat.getvalue('empid')

def contactman(empid):
	mydb = MySQLdb.connect('localhost', 'root','d3fault', 'contact')
	mycurs = mydb.cursor()
	if empid == 'allemp':
		myf = open('v1/contacts.json','r')
		myd = myf.read()
		return json.loads(myd)
		myf.close()
	elif empid == empid:
                quer = "select empid, name, email_id, phnum, team, p_oncall, s_oncall, manager, manid from contactman where empid='%s'" %(empid)
                mycurs.execute(quer)
                dat = mycurs.fetchall()
                contacts = {}
                for i in dat:
                        dictcon = {}
                        dictcon['name'] = i[1]
                        dictcon['Email'] = i[2]
                        dictcon['PhoneNumber'] = i[3]
                        dictcon['Team'] = i[4]
                        dictcon['Manager'] = i[7]
                        dictcon['ManagerID'] = i[8]
                        if i[5] == 'y':
                                dictcon['PrimaryOncall'] = 'Yes'
                        else:
                                dictcon['PrimaryOncall'] = 'No'
                        if i[6] == 'y':
                                dictcon['SecondaryOncall'] = 'Yes'
                        else:
                                dictcon['SecondaryOncall'] = 'No'
                        contacts[i[0]] = dictcon
		return json.dumps(contacts)

        mydb.close()

if empid == None:
	print "Content-Type: text/plain"
	print
	print "go Home, you are drunk. There is no API here"	
elif empid == 'allemp':
	print "Content-Type: text/plain"
	print
	print contactman('%s' %(empid))
elif empid == empid:
	print "Content-Type: text/plain"
	print
	print contactman('%s' %(empid))
