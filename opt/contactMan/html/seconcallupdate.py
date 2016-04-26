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

	if s_oncall == seccall:
		print "<p>There were no changes found. You data remains unchanged </p>"
        	print "<p>This page will redirect you to the homepage in few seconds. <br>Else click <a href='index.py'>here</a> </p>"
	else:
        	if s_oncall != seccall:
			conn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
			seccurse = conn.cursor()
                	seascall = "select empid, name from contactman where team='%s' and s_oncall='y'" %(team)
                	seccurse.execute(seascall)
                	curscall = seccurse.fetchall()
                	if  primcall == 'y' and s_oncall == 'y':
                        	print "<p> You cannot be both primary and secondary on-call. Please ask your colleagues to take over the primary oncall task </p>"
        			print "<p>This page will redirect you to the homepage in few seconds. <br>Else click <a href='index.py'>here</a> </p>"
               		else:
                        	if len(curscall) > 0:
                                	quer = 'update contactman set s_oncall="y" where empid="%s"' %(empid)
                                	seccurse.execute(quer)
                                	conn.commit()
                                	upt = 'update contactman set updated_date=current_timestamp() where empid="%s"' %(empid)
                                	seccurse.execute(upt)
                                	conn.commit()
                                	rmscall = 'update contactman set s_oncall = NULL where empid="%s"' %(curscall[0][0])
                                	seccurse.execute(rmscall)
                                	conn.commit()
                                	print '<p>You have been made the secondary oncall - replacing %s</p>' %(curscall[0][1])
        				print "<p>This page will redirect you to the homepage in few seconds. <br>Else click <a href='index.py'>here</a> </p>"
                                	conn.close()
					logger.seconcall(username)
                        	else:
                                	quer = 'update contactman set s_oncall="y" where empid="%s"' %(empid)
                                	seccurse.execute(quer)
                                	conn.commit()
                                	upt = 'update contactman set updated_date=current_timestamp() where empid="%s"' %(empid)
                                	seccurse.execute(upt)
                                	conn.commit()
                                	print '<h2>You are now the secondary on-call</h2>'
        				print "<p>This page will redirect you to the homepage in few seconds. <br>Else click <a href='index.py'>here</a> </p>"
                                	conn.close()
					logger.seconcall(username)
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
