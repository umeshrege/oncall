#!/usr/bin/python

import cgi
import cgitb
import myapi
import MySQLdb
import os
import Cookie
import logger

cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')
try:
	cookie.load(ifcookie)
        username = cookie['username'].value
except:
	pass

dat = cgi.FieldStorage()
empid = dat.getvalue('empid')
name = dat.getvalue('name')
email = dat.getvalue('email')
phnum = dat.getvalue('phnum')
team = dat.getvalue('team')
manager = dat.getvalue('manager')
manid = dat.getvalue('manid')
if dat.getvalue('oncall') == "pri-oncall" :
	p_oncall = 'y'
	s_oncall = 'null'
elif dat.getvalue('oncall') == "sec-oncall": 
	p_oncall = 'null'
	s_oncall = 'y'
else:
	p_oncall = 'null'
	s_oncall = 'null'

mydb = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
mycurs = mydb.cursor()


if not ifcookie:
        print """Content-type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <meta http-equiv="refresh" content="0; url=http://oncall.nm.4x3i.com" />
</head>
<body></body>
</html>
"""

elif ifcookie and len(username) > 0:
	print"""Content-Type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <meta http-equiv="refresh" content="5; url=https://oncall.nm.4x3i.com/" />
</head>

<body>

<div class="title">
        <div id="header">
                <p><a href="index.py">4x3i OnCall Search</a></p>
        </div>
        <div id="titlenav">
                <ul>
                        <li></li>
                </ul>
        </div>
</div>

	<div class="search">
"""
	if p_oncall == 'null' and s_oncall == 'null':
		checkemp = "select empid from contactman where empid='%s'" %(empid)
		mycurs.execute(checkemp)
		ifempexist = mycurs.fetchall()
		if len(ifempexist) > 0:
			print '<h2>You are already a registered used. If you are attempting to update, click <a href="update.py">here</a></h2>'
		else:
        		quer = "insert into contactman(empid, name, email_id, phnum, team, manager, updated_date, manid) values('%s', '%s', '%s', '%s', '%s', '%s', current_timestamp(), '%s')" %(empid, name, email, phnum, team, manager, manid)
			addme = mycurs.execute(quer)
			mydb.commit()
			mydb.close()
			print '<p>%s has been added to the database</p>' %(name)
			logger.register(username)
	elif p_oncall == 'y':
		seapcall = "select empid, name from contactman where team='%s' and p_oncall='y'" %(team)
		mycurs.execute(seapcall)
		curpcall = mycurs.fetchall()
		if len(curpcall) > 0:
			quer = "insert into contactman(empid, name, email_id, phnum, team, p_oncall, manager, updated_date) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', current_timestamp())" %(empid, name, email, phnum, team, p_oncall, manager)
			mycurs.execute(quer)
			mydb.commit()
			rmpcall = 'update contactman set p_oncall = NULL where empid="%s"' %(curpcall[0][0])
			mycurs.execute(rmpcall)
			mydb.commit()
			print '<p>%s has been added to the database</p>' %(name)
			print '<p>You have been made the primary oncall - replacing %s</p>' %(curpcall[0][1])
			logger.register(username, addi="and made the primary oncall")
		else:
			quer = "insert into contactman(empid, name, email_id, phnum, team, p_oncall, manager, updated_date) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', current_timestamp())" %(empid, name, email, phnum, team, p_oncall, manager)
                	mycurs.execute(quer)
			print '<p>You have been added to the database and also made the primary-onCall</p>'
                	mydb.commit()
			logger.register(username, addi="and made the primary oncall")
		mydb.close()
	elif s_oncall == 'y':
        	seascall = "select empid, name from contactman where team='%s' and s_oncall='y'" %(team)
        	mycurs.execute(seascall)
        	curpcall = mycurs.fetchall()
        	if len(curpcall) > 0:
                	quer = "insert into contactman(empid, name, email_id, phnum, team, s_oncall, manager, updated_date) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', current_timestamp())" %(empid, name, email, phnum, team, s_oncall, manager)
                	mycurs.execute(quer)
                	mydb.commit()
                	rmscall = 'update contactman set s_oncall = NULL where empid="%s"' %(curpcall[0][0])
                	mycurs.execute(rmscall)
                	mydb.commit()
                	print '<p>%s has been added to the database</p>' %(name)
                	print '<p>You have been made the secondary oncall - replacing %s</p>' %(curpcall[0][1])
			logger.register(username, addi="and made the secondary oncall")
        	else:
                	quer = "insert into contactman(empid, name, email_id, phnum, team, s_oncall, manager, updated_date) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', current_timestamp())" %(empid, name, email, phnum, team, s_oncall, manager)
                	mycurs.execute(quer)
                	mydb.commit()
			print "<p>You has been added to the database and also made the secondary on-call</p>"
			logger.register(username, addi="and made the secondary oncall")
        	mydb.close()

	print """
        </div>
</div>
</body>
</html>
	"""

myapi.contactman()
