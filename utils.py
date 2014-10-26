#!/usr/bin/env python

import cgi
import cgitb
from thermometer import thermometerRead
from scale import *

cgitb.enable()
form = cgi.FieldStorage()
function=form.getvalue("function")

if (function == "temperature"): 
  print(thermometerRead("28-00042d367bff"))

if (function == "weight"): 
  scaleInit()
  print(rawdata2g(scaleRead()))

