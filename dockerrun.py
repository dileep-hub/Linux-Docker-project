#!/usr/bin/python3
print("content-type:text/html")
print()
import cgi
import subprocess as sp
form = cgi.FieldStorage()
#osname = input("enter the os name: ")
osname = form.getvalue("x")
osimage = form.getvalue("i")
cmd = "sudo docker run -d -i  -t --name {0} {1}".format(osname,osimage)
output = sp.getstatusoutput(cmd)
status = output[0]

out = output[1]
if status == 0:
    print("Os named {} has been launched".format(osname))
else:
    print("some error occured: {}".format(out))
