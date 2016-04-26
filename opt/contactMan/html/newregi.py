#!/usr/bin/python

import os
import Cookie
import MySQLdb

cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')
dbconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
dbcur = dbconn.cursor()
quer = "select * from team"
dbcur.execute(quer)
fetcher = dbcur.fetchall()
dbteams = []
for i in fetcher:
        dbteams.append(i[0])

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
        cookie.load(ifcookie)
        username = cookie['username'].value
        name = cookie['name'].value
        empid = cookie['empid'].value
        if len(username) > 0 and len(name) > 0:
		print """Content-type: text/html\n\n\r

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
                <li><a href="index.py">Home &#9662;</a>
                <ul class="dropdown">
                <li><a href="newregi.py">Register</a></li>
                <li><a href="update.py">Update</a></li>
                <li><a href="logout.py">Logout</a></li>
                </ul> 
	</div>
</div>

<div class="search">
<h1>Enter your details</h1>
	<div id="searchfield">
	<form action="mrburns.py" method="POST">
		<font size="2"> EmpID: </font><input type="number"  name="empid" class="reginput" value="%s" readonly><br><br>
		<font size="2">  Team: </font><input type="text" name="team" class="reginput" placeholder="Team" id="autocomplete"  required><br><br>
		<font size="2"> Primary On-call </font><input type="radio" name="oncall" value="pri-oncall">
		<font size="2"> Secondary On-call </font><input type="radio" name="oncall" value="sec-oncall">
 		<br>
		<br>
		<input value="Continue" type="submit"><br>
		<p style="font-size: 10px;margin-left: 3px;">*It is not mandatory to select primary or secondary on-call radio buttons</p>
	</form>
	</div>
</div>
</body>
</html>
""" %(dbteams, empid)
	else:
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

dbconn.close()
