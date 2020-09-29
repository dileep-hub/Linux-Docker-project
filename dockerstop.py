#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

form1 = cgi.FieldStorage()
os = form1.getvalue("d")

cmd1 = "sudo docker stop {}".format(os)

run1 = sp.getstatusoutput(cmd1)
status1 = run1[0]
osp = run1[1]


if status1 == 0:
    print("Your Docker os has stopped..{}".format(os))
else:
    print("error")
