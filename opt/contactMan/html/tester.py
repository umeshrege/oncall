#!/usr/bin/python

import Cookie
import os
import MySQLdb

teamconn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
teamcur = conn.cursor()
quer = "select * from team"
teamcur.execute(quer)
fetcher = teamcur.fetchall()
dbteams = []
for i in fetcher:
	dbteams.append(i[0])

print """Content-Type: text/html\n\n\r
<html>
<head>
        <title>4x3i Tech YellowPage</title>
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
"""%dbteams

print dbteams

print """

<form>
  <input type="text" id="MyQuery" placeholder="Search resources" name="q"> 
  <input type="radio" onclick="ModifyPlaceHolder(this)" id="All" name="s.cmd" checked> All
  <input type="radio" onclick="ModifyPlaceHolder(this)" id="Books" name="s.cmd"> Books
</form>

</body>
</html>
"""
conn.close()
