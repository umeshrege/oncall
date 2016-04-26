#!/usr/bin/python

import cgi
import cgitb
import MySQLdb


dat = cgi.FieldStorage()
seatype = dat.getvalue('typesearch')
mydb = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
mycurs = mydb.cursor()

print """Content-Type: text/html\n\n\r
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
		</ul>
	</div>
</div>

<div class="search">
<div class="sresult"> 
"""
if seatype == 'emp_search':
	name = dat.getvalue('empsearch')
	quer = "select name, team, email_id, phnum, manager, manid from contactman where name like " +str('\'%')+name+str('%\'')
	mycurs.execute(quer)
	myout = mycurs.fetchall()
	if len(myout) > 0:
                print """<p id='restitle' style="margin-left: 3px; color: red;"> Search result for the user "%s"<br>
		Note: Click on the manager's name to get his/her details.
		</p><br><br>""" %(name)
                for i in range(len(myout)):
                        print "<form><fieldset>"
                        print "<legend>"+str(myout[i][0])+"</legend>"
                        print "<table>"
                        print "<tbody>"
                        print "<tr>"
                        print "<td>Name</td>"
                        print "<td>"+" "+str(myout[i][0])+"</td>"
                        print "</tr>"
                        print "<tr>"
                        print "<td>Team</td>"
                        print "<td>"+" "+str(myout[i][1])+"</td>"
                        print "</tr>"
                        print "<tr>"
                        print "<td>Email Address</td>"
                        print "<td>"+" "+str(myout[i][2])+"</td>"
                        print "</tr>"
                        print "<tr>"
                        print "<td>Phone Number</td>"
                        print "<td>"+" "+str(myout[i][3])+"</td>"
                        print "</tr>"
                        print "<tr>"
                        print "<td>Reporting Manager</td>"
                        print "<td>"+"<a href='searchme.py?empsearch="+str(myout[i][4])+"&typesearch=emp_search'>"+" "+str(myout[i][4])+"</a></td>"
                        print "</tr>"
                        print "</tbody>"
                        print "</table>"
                        print "</form></fieldset>"
	else:
		print "<h2>Our database does not contain a user by the name "+str(name)+ "</h2>"
elif seatype == 'oncall_search':
	name = dat.getvalue('empsearch')
	quer = "select name, email_id, phnum, p_oncall, s_oncall, manager from contactman where team='%s' and (p_oncall='y' or s_oncall='y')" %(name)
	mycurs.execute(quer)
	myout = mycurs.fetchall()
	if len(myout) > 0:
                print """<p id='restitle' style="margin-left: 3px; color: red;"> On-Call search result for the team "%s"<br>
                Note: Click on the manager's name to get his/her details.
                </p>""" %(name)
		print """<textarea rows="6" cols="90" style="margin-left: 3px;">
- If Primary On-call is not responding, escalate to secondary-Oncall
- If Secondary on-call is not responding, go to secondary-oncall's manager. 
- Follow up with an email and wait for a response for 30 minutes.
- If there is no response from the manager, go to the secondary escalation manager.
- Follow up with an email to keep the transcations documented.
</textarea><br><br>"""
                for i in range(len(myout)):
                        print "<form><fieldset>"
			if myout[i][3] == 'y' and myout[i][4] == None:
                        	print "<legend>PRIMARY ON-CALL</legend>"
			elif myout[i][4] == 'y' and myout[i][3] == None:
                        	print "<legend>SECONDARY ON-CALL</legend>"
                        print "<table>"
                        print "<tbody>"
                        print "<tr>"
                        print "<td>Name</td>"
                        print "<td>"+str(myout[i][0])+"</td>"
                        print "</tr>"
                        print "<tr>"
                        print "<td>Email Address</td>"
                        print "<td>"+str(myout[i][1])+"</td>"
                        print "</tr>"
                        print "<tr>"
                        print "<td>Phone Number</td>"
                        print "<td>"+str(myout[i][2])+"</td>"
                        print "</tr>"
                        print "<tr>"
                        print "<td>Manager</td>"
                        print "<td>"+"<a href='searchme.py?empsearch="+str(myout[i][5])+"&typesearch=emp_search'>"+str(myout[i][5])+"</a></td>"
                        print "</tr>"
                        print "</tbody>"
                        print "</table>"
                        print "</form></fieldset>"
	else:
		print "<h2>There is no designated primary/secondary oncall for the team '%s'</h2>" %(name)

print"""
</div>
</div>
</body>
</html>
"""

mydb.close()
