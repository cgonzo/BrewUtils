#!/usr/bin/env python

import cgi
import cgitb
from thermometer import thermometerRead

form = cgi.FieldStorage()
function=form.getvalue("function")

if (function == "temperature"): 
  print(thermometerRead("28-00042d367bff"))

