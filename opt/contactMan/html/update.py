#!/usr/bin/python

import os
import Cookie

cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')
try:
        cookie.load(ifcookie)
        username = cookie['username'].value
        name = cookie['name'].value
	empid = cookie['empid'].value
except:
	pass

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
		print """Content-Type: text.py\n\n\r
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
                <li><a href="index.py">Home &#9662;</a>
                <ul class="dropdown">
                <li><a href="newregi.py">Register</a></li>
                <li><a href="update.py">Update</a></li>
                <li><a href="logout.py">Logout</a></li>
                </ul> 
	</div>
</div>

<div class="search">
<h1>Update your data</h1>
	<div id="searchfield">
	<form action="updateme.py" method="POST">
		<font size="2"> Employee ID: </font>
		<input style="width: 200px" autocomplete="off" name="empid" class="reginput" id="autocomplete" autofocus="" type="number" value="%s" readonly>
		<select name="myedit" required>
		<option value="phnum">Phone Number</option>
		<option value="p_oncall">Primary Oncall</option>
		<option value="s_oncall">Secondary Oncall</option>
		<option value="team">Team</option>
		</select>
		<br>
		<br>
		<input value="Continue" type="submit"><br>
	</form>
	</div>
</div>
</body>
</html>
""" %(empid)
