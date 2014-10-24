#!/usr/bin/env python

import hid
import time

def scaleInit():
    global h
    try:
        print "Opening device"
        h = hid.device()
        h.open(0x4d9, 0x8010)
    
        print "Manufacturer: %s" % h.get_manufacturer_string()
        print "Product: %s" % h.get_product_string()
        print "Serial No: %s" % h.get_serial_number_string()
        return 1
    except IOError, ex:
        print ex
        print "You probably don't have the hard coded test hid. Update the hid.device line"
        print "in this script with one from the enumeration list output above and try again."
        return 0

def scaleOn():
    h.send_feature_report([0, 0xa0, 0xde, 0xa0, 0, 0, 0, 0, 0])

def scaleSetLb():
    h.send_feature_report([0, 0xa0, 0x6e, 0xa0, 0, 0, 0, 0, 0])

def scaleSetLbOz():
    h.send_feature_report([0, 0xa0, 0x5e, 0xa0, 0, 0, 0, 0, 0])

def scaleSetKg():
    h.send_feature_report([0, 0xa0, 0x7e, 0xa0, 0, 0, 0, 0, 0])

def scaleRead():
    h.send_feature_report([0x00, 0x90, 0xfe, 0x80, 0xff, 0x7f, 0x00, 0x00, 0x03])
    return h.read(9)

def rawdata2g( arr ):
    return (arr[2]>>4 & 0xf)*10000+(arr[2] & 0xf)*1000+(arr[1]>>4 & 0xf)*100+(arr[1] & 0xf)*10


scaleInit()
scaleOn()
scaleSetKg()
while 1:
    data = scaleRead()
    print data
    print rawdata2g(data)
    time.sleep(0.05)

    
print "Closing device"
h.close()


print "Done"
