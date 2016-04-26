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

elif (ifcookie and len(username) > 0) and empid == cookemp:
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

	if p_oncall == primcall:
		print "<h2>There were no changes found. You are already the primary on-call. </h2>"
		print "<p>This page will redirect you to the homepage in few seconds. <br>Else click <a href='index.py'>here</a> </p>"
	else:
		if p_oncall != primcall:
        		seapcall = "select empid, name from contactman where team='%s' and p_oncall='y'" %(team)
			mycurs.execute(seapcall)
        		curpcall = mycurs.fetchall()
        		if  seccall == 'y' and p_oncall == 'y':
                		print "<p> You cannot be both primary and secondary on-call. Please ask your colleagues to take over the secondary oncall task </p>"
        		else:
                		if len(curpcall) > 0:
                        		quer = 'update contactman set p_oncall="y" where empid="%s"' %(empid)
                        		mycurs.execute(quer)
                        		mydb.commit()
                        		upt = 'update contactman set updated_date=current_timestamp() where empid="%s"' %(empid)
                        		mycurs.execute(upt)
                        		mydb.commit()
                        		rmpcall = 'update contactman set p_oncall = NULL where empid="%s"' %(curpcall[0][0])
                        		mycurs.execute(rmpcall)
                        		mydb.commit()
                        		print '<p>You have been made the primary oncall - replacing %s</p>' %(curpcall[0][1])
					print "<p>This page will redirect you to the homepage in few seconds. <br>Else click <a href='index.py'>here</a> </p>"
                        		mydb.close()
					logger.primoncall(username)
               			else:
                        		quer = 'update contactman set p_oncall="y" where empid="%s"' %(empid)
                        		mycurs.execute(quer)
                        		mydb.commit()
                        		upt = 'update contactman set updated_date=current_timestamp() where empid="%s"' %(empid)
                        		mycurs.execute(upt)
                        		mydb.commit()
                        		print '<p>%s --> You are now the primary on-call</p>' %(name)
					print "<p>This page will redirect you to the homepage in few seconds. <br>Else click <a href='index.py'>here</a> </p>"
                        		mydb.close()
					logger.primoncall(username)
		else:
			pass

	print """
        </div>
</div>
</body>
</html>
	"""
	myapi.contactman()
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
