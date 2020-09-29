#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

a = ["dileep-hub"]
b = ["Dileep@123"]

form = cgi.FieldStorage()
user  = form.getvalue('user')
passwd = form.getvalue('passwd')
if(user in a):
    if(passwd in b):
        final = sp.getoutput("cat  /var/www/html/cmd.html")
    else:
        print("invalid password")

else:
    print("invalid username")

print(final)
