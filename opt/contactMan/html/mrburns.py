#!/usr/bin/python

import cgi
import cgitb
import myapi
import MySQLdb
import os
import Cookie
import json
import urllib2
import getmanager

cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')
try:
	if ifcookie:
        	cookie.load(ifcookie)
     		username = cookie['username'].value
	else:
        	pass
except:
	pass

dat = cgi.FieldStorage()
empid = dat.getvalue('empid')
team = dat.getvalue('team')

if dat.getvalue('oncall') == "pri-oncall" or dat.getvalue('oncall') == "sec-oncall":
        oncall = dat.getvalue('oncall')
else:
        oncall = 'NULL'

try:
	getfirst = urllib2.urlopen('http://org-dir.nm.4x3i.com:38700/employeeData/'+str(empid))
	myd = getfirst.read()
	myj = json.loads(myd)
except:
	print """Content-type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <meta http-equiv="refresh" content="3; url=http://oncall.nm.4x3i.com" />
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
<h2>Warning..!! That is not a Valid employee ID. Rerouting to homepage in 3..2..1</h2>
</div>
</body>
</html>
"""

name = myj['name'].encode('ascii', 'ignore')
email = myj['email'].encode('ascii', 'ignore')
phnum = myj['mobile'].encode('ascii', 'ignore')
manager = myj['manager'].encode('ascii', 'ignore')
manid = myj['managerId'].encode('ascii', 'ignore')
getmanager.sneaker(myj['managerId'].encode('ascii', 'ignore'))

mydb = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
mycurs = mydb.cursor()
checkemp = "select empid from contactman where empid='%s'" %(empid)
mycurs.execute(checkemp)
ifempexist = mycurs.fetchall()

if not ifcookie or len(username) == 0:
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

elif ( ifcookie and len(username) >0 ) and len(ifempexist) == 0:
	print"""Content-Type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
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
<h2>Warning..!! Please check before Confirming</h2>
        <div id="searchfield">
        <form action="regme.py" method="POST">
                <font size="2"> EmpID: </font><input type="number"  name="empid" class="reginput" value="%s" readonly><br><br>
                <font size="2">  Name: </font><input type="text"  name="name" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Email: </font><input type="email"  name="email" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Phone: </font><input type="number"  name="phnum" class="reginput" maxlength="12" value="%s"><br><br>
                <font size="2">  Team: </font><input type="text"  name="team" class="reginput" value="%s"  readonly><br><br>
                <font size="2">  Manager: </font><input type="text"  name="manager" class="reginput" value="%s"  readonly><br><br>
                <font size="2" style=" display: none; ">  Manager ID: </font><input type="text"  name="manid" class="reginput" value="%s" readonly style="
    display: none;
">
"""%(empid, name, email, phnum, team, manager, manid)
	dbconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
	dbcur = dbconn.cursor()
	quer = "select * from team"
	dbcur.execute(quer)
	fetcher = dbcur.fetchall()
	dbteams = []
	for i in fetcher:
        	dbteams.append(i[0])
	if team not in dbteams:
		quer = "insert into team(team) values('%s')"%(team)
		dbcur.execute(quer)
		dbconn.commit()
	dbconn.close()
	if oncall == 'pri-oncall':
		print '<font size="2"> Primary On-call </font><input type="radio" name="oncall" value="pri-oncall" checked>'
	      	print '<font size="2"> Secondary On-call </font><input type="radio" name="oncall" value="sec-oncall"><br><br><input value="Submit" type="submit"><br> '
	elif oncall == 'sec-oncall':
		print '<font size="2"> Primary On-call </font><input type="radio" name="oncall" value="pri-oncall">'
	      	print '<font size="2"> Secondary On-call </font><input type="radio" name="oncall" value="sec-oncall" checked><br><br><input value="Submit" type="submit"><br> '
	else:
		print '<br><br><input value="Submit" type="submit"><br>'	
	print """
        </div>
        </div>
</div>
</body>
</html>
"""
elif ( ifcookie and len(username) >0 ) and len(ifempexist) != 0:
	print """Content-Type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
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
<h2>Warning..!! This employee ID already exists in our database. <br>If you are attempting to update your data, please go <a href="update.py">here</a></h2>
        </div>
        </div>
</div>
</body>
</html>
"""

mydb.close()
myapi.contactman()
