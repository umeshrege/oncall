#!/usr/bin/python

import MySQLdb
from logger import Delteam

conn = MySQLdb.connect('localhost', 'root', 'd3fault', 'contact')
curs = conn.cursor()
quer = "select distinct(team) from contactman where team != 'None'"
curs.execute(quer)
conman = curs.fetchall()
cTable = []
for i in conman:
	cTable.append(i[0])


tque = "select team from team"
curs.execute(tque)
ctea =  curs.fetchall()
tteam = []
for i in ctea:
	tteam.append(i[0])


for i in tteam:
	if i not in cTable:
		quer = "delete from team where team='%s'" %(i)
		curs.execute(quer)
		conn.commit()
		Delteam(i)

conn.close()
