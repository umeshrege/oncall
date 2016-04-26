#!/usr/bin/python

import cgi
import cgitb
import myapi
import MySQLdb
import os
import Cookie

cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')


dat = cgi.FieldStorage()
empid = dat.getvalue('empid')
name = dat.getvalue('name')
email = dat.getvalue('email')
phnum = dat.getvalue('phnum')
team = dat.getvalue('team')
if dat.getvalue('oncall') == "pri-oncall" or dat.getvalue('oncall') == "sec-oncall":
        oncall = dat.getvalue('oncall')
else:
        oncall = 'NULL'

mydb = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
mycurs = mydb.cursor()
checkemp = "select empid from contactman where empid='%s'" %(empid)
mycurs.execute(checkemp)
ifempexist = mycurs.fetchall()

if not ifcookie or empid == None:
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



if len(ifempexist) == 0:
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
                <font size="2"> Phone: </font><input type="number"  name="phnum" class="reginput" maxlength="12" value="%s" readonly><br><br>
                <font size="2">  Team: </font><input type="text"  name="team" class="reginput" value="%s"  readonly><br><br>
"""%(empid, name, email, phnum, team)

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

elif len(ifempexist) != 0:
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
