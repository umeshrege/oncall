#!/usr/bin/python

import Cookie
import cgi
import cgitb
import os

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
		<input autocomplete="off" name="empname" class="biginput" id="autocomplete" autofocus="" type="text" required="">
    	<font size="2"> Password: </font>
		<input autocomplete="off" name="emppass" class="biginput" id="autocomplete" autofocus="" type="password" required="">    
		<input value="login" type="submit"><br>
	</form>
	</div>
</div>

<div class="search">
<h1>On-Call Search</h1>
	<div id="searchfield">
<script>
function ModifyPlaceHolder(element) {
  var data = {
    oncall_search: 'Search resources',
    emp_search: 'Search books e.g. Harry Potter',
  };
  var input = element.form.autocomplete;
  input.placeholder = data[element.id];
}
</script>

	<form action="searchme.py" method="POST">
		<font size="2"> Name: </font>
		<input autocomplete="off" name="empsearch" id="autocomplete" type="text" placeholder="Search resources" required><br><br>
		<input type="radio" name="typesearch" onclick="ModifyPlaceHolder(this) value="oncall_search" id="oncall_search" checked="checked">On-Call Search
		<input type="radio" name="typesearch" onclick="ModifyPlaceHolder(this) value="emp_search" id="emp_search">Employee Search
 		<br>
		<br>
		<input value="Submit" type="submit"><br>
	</form>
	</div>
</div>
</body>
</html>
"""
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
""" 
		else:
			print """Content-Type: text/html\n\n\r
<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
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
                <input autocomplete="off" name="empname" class="biginput" id="autocomplete" autofocus="" type="text" required="">
        <font size="2"> Password: </font>
                <input autocomplete="off" name="emppass" class="biginput" id="autocomplete" autofocus="" type="password" required="">    
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
"""
else:
	print """Content-Type: text/html\n\n\r
<html>
<head>
        <title>4x3i OnCall Search</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
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
                <input autocomplete="off" name="empname" class="biginput" id="autocomplete" autofocus="" type="text" required="">
        <font size="2"> Password: </font>
                <input autocomplete="off" name="emppass" class="biginput" id="autocomplete" autofocus="" type="password" required="">    
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
"""
