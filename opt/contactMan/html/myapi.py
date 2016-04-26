#!/usr/bin/python

import MySQLdb
import json

def contactman():
        mydb = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
        mycurs = mydb.cursor()
        quer = "select empid, name, email_id, phnum, team, p_oncall, s_oncall from contactman"
        mycurs.execute(quer)
        dat = mycurs.fetchall()
        contacts = {}
        for i in dat:
                dictcon = {}
                dictcon['name'] = i[1]
                dictcon['Email'] = i[2]
                dictcon['PhoneNumber'] = i[3]
                dictcon['Team'] = i[4]
                if i[5] == 'y':
                        dictcon['PrimaryOncall'] = 'Yes'
                else:
                        dictcon['PrimaryOncall'] = 'No'
                if i[6] == 'y':
                        dictcon['SecondaryOncall'] = 'Yes'
                else:
                        dictcon['SecondaryOncall'] = 'No'
                contacts[i[0]] = dictcon
        mydb.close()

	myjson = open('v1/contacts.json', 'w')
	payload = json.dumps(contacts)
	myjson.write(payload)
	myjson.close()

if __name__ == "__main__":
	print "you cannot run this directly"
else:
	contactman()
