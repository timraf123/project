


import cgi
import sqlite3


print("Content-type:text/html\r\n")

form = cgi.FieldStorage()

un= form.getvalue("un")
up = form.getvalue("pwd")
print("<script>window.location.href='http://localhost:8000/form.html';</script>")

#if un=="chandu" and up=="519":
#	print("<script>window.location.href='http://localhost:8000/form.html';</script>")
#else:
#WS


