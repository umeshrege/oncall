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

if ifcookie:
        cookie.load(ifcookie)
        username = cookie['username'].value
        cookemp = cookie['empid'].value
else:
        pass


dat = cgi.FieldStorage()
empid = dat.getvalue('empid')
name = dat.getvalue('name')
email = dat.getvalue('email')
phnum = dat.getvalue('phnum')
team = dat.getvalue('team')
if dat.getvalue('oncall') == "pri-oncall" :
	p_oncall = 'y'
	s_oncall = 'null'
elif dat.getvalue('oncall') == "sec-oncall": 
	p_oncall = 'null'
	s_oncall = 'y'
else:
	p_oncall = 'null'

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

elif (ifcookie and len(username) > 0) and empid == cookemp:
	print"""Content-Type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <meta http-equiv="refresh" content="2; url=https://oncall.nm.4x3i.com/" />
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

	quer = 'select phnum, p_oncall, s_oncall from contactman where empid="%s"' %(empid)
	mycurs.execute(quer)
	mystat = mycurs.fetchall()

	if mystat[0][1] == None:
		primcall = 'null'
	else:
		primcall = mystat[0][1]
	if mystat[0][2] == None:
		seccall = 'null'
	else:
		seccall = mystat[0][2]


	if phnum == mystat[0][0]:
		print "<h2>There were no changes found. You data remains unchanged</h2>"
	else:
		if phnum != mystat[0][0]:
                	phupda = 'update contactman set phnum="%s" where empid="%s"' %(phnum, empid)
                	mycurs.execute(phupda)
                	mydb.commit()
                	upt = 'update contactman set updated_date=current_timestamp() where empid="%s"' %(empid)
                	mycurs.execute(upt)
                	mydb.commit()
			logger.phone(username)
                	print '<p>You phone number has been updated.</p>'
                	mydb.close()
			myapi.contactman()
			pass

	print """
        </div>
</div>
</body>
</html>
"""
else:
	print """Content-type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <meta http-equiv="refresh" content="2; url=http://oncall.nm.4x3i.com/logout.py" />
</head>
<body>
<div class="title">
        <div id="header">
                <p><a href="index.py">4x3i OnCall Search</a></p>
        </div>
        <div id="titlenav">
                <ul>
                </ul>
        </div>
</div>

<div class="search">
<div class="sresult"> 
<h2> Not a decent thing to do smart boy. Get out now. </h2>

</div>
</div>



</body>
</html>
"""
