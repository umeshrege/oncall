#!/usr/bin/python

import Cookie
import cgi
import cgitb
import os
import MySQLdb

dbconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
dbcur = dbconn.cursor()
quer = "select * from team"
dbcur.execute(quer)
fetcher = dbcur.fetchall()
dbteams = []
for i in fetcher:
        dbteams.append(i[0])


cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')
if ifcookie:
	ck = ifcookie.split(';')
	handler = {}
	for cookie in ck:
		cookie = cookie.split('=')
		handler[cookie[0]] = cookie[1]

	if ' username' not in handler.keys():
		print """Content-Type: text/html\n\n\r
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
	<div id="loghead">
	</div>
	<div id="header">
		<p><a href="index.py">4x3i OnCall Search</a></p>
	</div>
	<div id="titlenav">
	<form id = "nologin" action="login.py" method="POST">
		<font size="2"> Username: </font>
		<input autocomplete="off" name="empname" class="biginput" autofocus="" type="text" required="">
    	<font size="2"> Password: </font>
		<input autocomplete="off" name="emppass" class="biginput" autofocus="" type="password" required="">    
		<input value="login" type="submit"><br>
	</form>
	</div>
</div>

<div class="search">
<h1>On-Call Search</h1>
	<div id="searchfield">
	<form action="searchme.py" method="POST">
		<font size="2"> Name: </font>
		<input autocomplete="off" name="empsearch" class="biginput" id="autocomplete" autofocus="" type="text" required><br><br>
		<input type="radio" name="typesearch" value="oncall_search" checked="checked">On-Call Search
		<input type="radio" name="typesearch" value="emp_search">Employee Search
 		<br>
		<br>
		<input value="Submit" type="submit"><br>
	</form>
	</div>
</div>
</body>
</html>
""" %dbteams
	else:
		cookie = Cookie.SimpleCookie()
		ifcookie = os.environ.get('HTTP_COOKIE')
	      	cookie.load(ifcookie)
       		username = cookie['username'].value
        	name = cookie['name'].value
		if len(username) > 0 and len(name) > 0:
			print """Content-Type: text/html\n\n\r
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
        <div id="loghead">
        </div>
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
<h1>On-Call Search</h1>
        <div id="searchfield">
        <form action="searchme.py" method="POST">
                <font size="2"> Name: </font>
                <input autocomplete="off" name="empsearch" class="biginput" id="autocomplete" autofocus="" type="text" required><br><br>
                <input type="radio" name="typesearch" value="oncall_search" checked="checked">On-Call Search
                <input type="radio" name="typesearch" value="emp_search">Employee Search
                <br>
                <br>
                <input value="Submit" type="submit"><br>
        </form>
        </div>
</div>
</body>
</html>
"""%dbteams
		else:
			print """Content-Type: text/html\n\n\r
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
        <div id="loghead">
        </div>
        <div id="header">
                <p><a href="index.py">4x3i OnCall Search</a></p>
        </div>
        <div id="titlenav">
        <form id="nologin" action="login.py" method="POST">
                <font size="2"> Username: </font>
                <input autocomplete="off" name="empname" class="biginput" autofocus="" type="text" required="">
        <font size="2"> Password: </font>
                <input autocomplete="off" name="emppass" class="biginput" autofocus="" type="password" required="">    
                <input value="login" type="submit"><br>
        </form>
        </div>
</div>

<div class="search">
<h1>On-Call Search</h1>
        <div id="searchfield">
        <form action="searchme.py" method="POST">
                <font size="2"> Name: </font>
                <input autocomplete="off" name="empsearch" class="biginput" id="autocomplete" autofocus="" type="text" required><br><br>
                <input type="radio" name="typesearch" value="oncall_search" checked="checked">On-Call Search
                <input type="radio" name="typesearch" value="emp_search">Employee Search
                <br>
                <br>
                <input value="Submit" type="submit"><br>
        </form>
        </div>
</div>
</body>
</html>
"""%dbteams
else:
	print """Content-Type: text/html\n\n\r
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
        <div id="loghead">
        </div>
        <div id="header">
                <p><a href="index.py">4x3i OnCall Search</a></p>
        </div>
        <div id="titlenav">
        <form id="nologin" action="login.py" method="POST">
                <font size="2"> Username: </font>
                <input autocomplete="off" name="empname" class="biginput" autofocus="" type="text" required="">
        <font size="2"> Password: </font>
                <input autocomplete="off" name="emppass" class="biginput" autofocus="" type="password" required="">    
                <input value="login" type="submit"><br>
        </form>
        </div>
</div>

<div class="search">
<h1>On-Call Search</h1>
        <div id="searchfield">
        <form action="searchme.py" method="POST">
                <font size="2"> Name: </font>
                <input autocomplete="off" name="empsearch" class="biginput" id="autocomplete" autofocus="" type="text" required><br><br>
                <input type="radio" name="typesearch" value="oncall_search" checked="checked">On-Call Search
                <input type="radio" name="typesearch" value="emp_search">Employee Search
                <br>
                <br>
                <input value="Submit" type="submit"><br>
        </form>
        </div>
</div>
</body>
</html>
"""%dbteams
dbconn.close()
