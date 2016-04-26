#!/usr/bin/python

import cgi
import cgitb
import MySQLdb
import os
import Cookie

cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')

dat = cgi.FieldStorage()
empid = dat.getvalue('empid')
myedit = dat.getvalue('myedit')

mydb = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
mycurs = mydb.cursor()
quer = 'select empid, name, email_id, phnum, team, p_oncall, s_oncall from contactman where empid="%s"' %(empid)
mycurs.execute(quer)
mydat = mycurs.fetchall()

dbconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
dbcur = dbconn.cursor()
quer = "select * from team"
dbcur.execute(quer)
fetcher = dbcur.fetchall()
dbteams = []
for i in fetcher:
        dbteams.append(i[0])
dbconn.close()

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

else:

	if len(mydat) > 0  and len(empid) > 0:
		print"""Content-Type: text/html\n\n\r

<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
        <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
        <script src="//code.jquery.com/jquery-1.10.2.js"></script>
        <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
<script>
  $(function() {
    var availableTags = %s;
    $( "#autocomplete" ).autocomplete({
      source: availableTags
    });
  });
  </script>
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
"""%dbteams
		if myedit == "phnum":
			print """
	<h2>You are about to update your phone number</h2>
        <div id="searchfield">
       <form action="phoneupdate.py" method="POST">
                <font size="2"> EmpID: </font><input type="number"  name="empid" class="reginput" value="%s" readonly><br><br>
                <font size="2">  Name: </font><input type="text"  name="name" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Email: </font><input type="email"  name="email" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Phone: </font><input type="number"  name="phnum" class="reginput" maxlength="12" value="%s"><br><br>
                <font size="2">  Team: </font><input type="text"  name="team" class="reginput" value="%s"  readonly><br><br>
                <input value="Submit" type="submit"><br>
        </form>
""" %(mydat[0][0], mydat[0][1], mydat[0][2], mydat[0][3], mydat[0][4])
		elif myedit == "p_oncall":
			print """
	<h2>You are about to designate yourself as the primary on-call</h2>
        <div id="searchfield">
       <form action="prioncallupdate.py" method="POST">
                <font size="2"> EmpID: </font><input type="number"  name="empid" class="reginput" value="%s" readonly><br><br>
                <font size="2">  Name: </font><input type="text"  name="name" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Email: </font><input type="email"  name="email" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Phone: </font><input type="number"  name="phnum" class="reginput" maxlength="12" value="%s" readonly><br><br>
                <font size="2">  Team: </font><input type="text"  name="team" class="reginput" value="%s"  readonly><br><br>
		<font size="2"> Primary On-call</font><input type="radio" name="oncall" value="pri-oncall" checked><br>
		<br>
                <input value="Submit" type="submit"><br>
        </form>
""" %(mydat[0][0], mydat[0][1], mydat[0][2], mydat[0][3], mydat[0][4])
		elif myedit == "s_oncall":
			print """
	<h2>You are about to designate yourself as the secondary on-call</h2>
        <div id="searchfield">
       <form action="seconcallupdate.py" method="POST">
                <font size="2"> EmpID: </font><input type="number"  name="empid" class="reginput" value="%s" readonly><br><br>
                <font size="2">  Name: </font><input type="text"  name="name" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Email: </font><input type="email"  name="email" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Phone: </font><input type="number"  name="phnum" class="reginput" maxlength="12" value="%s" readonly><br><br>
                <font size="2">  Team: </font><input type="text"  name="team" class="reginput" value="%s"  readonly><br><br>
                <font size="2"> Secondary On-call </font><input type="radio" name="oncall" value="sec-oncall" checked><br>
		<br>
                <input value="Submit" type="submit"><br>
        </form>
""" %(mydat[0][0], mydat[0][1], mydat[0][2], mydat[0][3], mydat[0][4])
		elif myedit == "team":
			print """
	<h2>You are about to update your team</h2>
        <div id="searchfield">
       <form action="teamupdate.py" method="POST">
                <font size="2"> EmpID: </font><input type="number"  name="empid" class="reginput" value="%s" readonly><br><br>
                <font size="2">  Name: </font><input type="text"  name="name" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Email: </font><input type="email"  name="email" class="reginput" value="%s" readonly><br><br>
                <font size="2"> Phone: </font><input type="number"  name="phnum" class="reginput" maxlength="12" value="%s" readonly><br><br>
                <font size="2">  Team: </font><input type="text"  name="team" class="reginput" id="autocomplete" value="%s" ><br><br>
		<br>
                <input value="Submit" type="submit"><br>
        </form>
""" %(mydat[0][0], mydat[0][1], mydat[0][2], mydat[0][3], mydat[0][4])


		print """ <br>
        </div>
        </div>
</div>
</body>
</html>
""" 
	else:
		print"""Content-Type: text/html\n\n\r

</html>
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
<h2></h2>
        <div id="searchfield">
	<h2>You are not a registered user. Click <a href='newregi.py'>here</a> to register.</h2>
        </div>
        </div>
</div>
</body>
</html>
"""

mydb.close()
