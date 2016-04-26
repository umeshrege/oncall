#!/usr/bin/python

import Cookie
import os
import cgi
import cgitb
import ldap
import logger
import MySQLdb


dbconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
dbcur = dbconn.cursor()
quer = "select * from team"
dbcur.execute(quer)
fetcher = dbcur.fetchall()
dbteams = []
for i in fetcher:
        dbteams.append(i[0])

dat = cgi.FieldStorage()
empid = dat.getvalue('empname')
emppass = dat.getvalue('emppass')

cookie = Cookie.SimpleCookie()
ifcookie = os.environ.get('HTTP_COOKIE')
if ifcookie and ifcookie != None:
        ck = ifcookie.split(';')
        handler = {}
        for cookie in ck:
                cookie = cookie.split('=')
                handler[cookie[0]] = cookie[1]

	if ' username' in handler.keys():
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
		try:
			ldap_server="login.nm.4x3i.com"
			username = empid
			password = emppass
			user_dn = "uid="+username+",ou=People,dc=4x3i,dc=com"
			base_dn = "dc=4x3i,dc=com"
			connect = ldap.open(ldap_server)
			search_filter = "uid="+username
			try:
				connect.bind_s(user_dn,password)
				result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
				login = True
				for i in result:
					uname = i[1]['uid'][0]
					empname = i[1]['gecos'][0]
					empid = i[1]['employeeNumber'][0]
				connect.unbind_s()
			except:
				connect.unbind_s()
				login = False 
		except:
			login = False

		if login == True:
			cookie = Cookie.SimpleCookie()
			cookie['username'] = uname
			cookie['name'] = empname
			cookie['empid'] = empid
			print cookie
			print  """Content-Type: text/html\n\n\r
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
			logger.login(uname)
		else:
			print  """Content-Type: text/html\n\n\r
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
        <div id="titlenav" style="color: white;">
        </div>
</div>

<div class="search">
<h2>incorrect username and password</h2>
<div id="searchfield">
<form action="login.py" method="POST">
                <font size="2"> Username: </font>
                <input autocomplete="off" name="empname" class="nologin" id="autocomplete" autofocus="" type="text" required=""><br>
        <font size="2"> Password: </font>
                <input autocomplete="off" name="emppass" class="nologin" id="autocomplete" autofocus="" type="password" required=""><br>    
                <input value="Submit" type="submit"><br>
        </form>
        </div>
        </div>
</div>
</body>
</html>
"""%dbteams
			logger.incorrect(empid)
elif ifcookie == None:
	try:
        	ldap_server="login.nm.4x3i.com"
                username = empid
                password = emppass
                user_dn = "uid="+username+",ou=People,dc=4x3i,dc=com"
                base_dn = "dc=4x3i,dc=com"
                connect = ldap.open(ldap_server)
                search_filter = "uid="+username
                try:
                	connect.bind_s(user_dn,password)
                        result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
                        login = True
                        for i in result:
                        	uname = i[1]['uid'][0]
                                empname = i[1]['gecos'][0]
                                empid = i[1]['employeeNumber'][0]
                        connect.unbind_s()
                except:
                	connect.unbind_s()
                        login = False
	except:
        	login = False

	if login == True:
        	cookie = Cookie.SimpleCookie()
                cookie['username'] = uname
                cookie['name'] = empname
                cookie['empid'] = empid
                print cookie
                print  """Content-Type: text/html\n\n\r
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
		logger.login(uname)
        else:
       		print  """Content-Type: text/html\n\n\r
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
        <div id="titlenav" style="color: white;">
        </div>
</div>

<div class="search">
<h2>incorrect username and password</h2>
<div id="searchfield">
<form action="login.py" method="POST">
                <font size="2"> Username: </font>
                <input autocomplete="off" name="empname" class="nologin" autofocus="" type="text" required=""><br>
        <font size="2"> Password: </font>
                <input autocomplete="off" name="emppass" class="nologin" autofocus="" type="password" required=""><br>    
                <input value="Submit" type="submit"><br>
        </form>
        </div>
        </div>
</div>
</body>
</html>
"""
		logger.incorrect(empid)

dbconn.close()
