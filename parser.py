#!/usr/bin/env python

import httplib
import json
from datetime import datetime
from StringIO import StringIO


__debug = True


HOST = "api.foursquare.com"
CLIENT_ID = "HPJBJ03G22E0YPJPP1WS1IL4TRG5QZE011QKXTA2MLHLYDSQ"
CLIENT_SEC = "K2Z5YKW3BTVT1CYMQ242HQO4YMS3DDUXNL4GBGOWDTK402K2"

# Fix the date format to match YYYYMMDD
d = datetime.now()
month = ""
day = ""

if d.month < 10:
    month = "0%s" % d.month

if d.day < 10:
    day = "0%s" % d.day

DATE = "%s%s%s" % (d.year, month, day)

# Create a userless url, using the client id, the client secret 
# and the current date in the specified format.
# More about userless: https://developer.foursquare.com/overview/auth.html
URL = "/v2/venues/search?ll=40.7,-74&client_id={client_id}&client_secret={client_secret}&v={date}".format(client_id=CLIENT_ID, client_secret=CLIENT_SEC, date=DATE)


if __debug:
    print URL, "\n\n"


try:
    import ssl
except ImportError:
    print "error: no ssl support"


def connect():
    connection = httplib.HTTPSConnection(HOST)
    connection.request("GET", URL)
    resp = connection.getresponse()
    connection.connect()

    # Choose the response.
    if resp.status == 200:
        read_response(resp)

    # Close the connection after the reception of data.
    connection.close()


def print_json(json_data):
    """Print the json_data"""
    print json.dumps(json_data, sort_keys=True, indent=4, separators=(",", ": "))


def read_response(response):
    """Get the response from the stream and print it."""
    data = response.read()
    if __debug:
        print data, "\n"
    #print_json(data)


if __name__ == "__main__":
    connect()


"""parser.py -- A parser for FourSquare data."""


__author__ = "ipinak"
__version__ = "0.1"
__copyright__ = "No copyright yet"

try:
    import threading
    from request import Request 
except ImportError as e:
    print "Some of your import does not exist"
    print "[Error occurred: %d - %s]" % (e.errno, e.strerror)


class FSQParser(threading.Thread):
    """
    Simple class to make a request to FourSquare API and retrieve
    data.
    """
    def __init__(self, request):
        if __debug: print "%s.__init__()" % (self.__class__.__name__)
        
        assert self.request.__class__.__name__ == Request.__class__.__name__
        self._request = request
        
        #def request():
        #    doc = "information about the request you want to make"
        #    
        #    def fget(self):
        #        return self._request
        #    
        #    def fset(self, request):
        #        self._request = request
        #
        #    def fdel(self):
        #        del self._request
        #        
        #    return locals()

    
    def __str__(self):
        return self.__class__.__name__


    def __unicode__(self):
        return self.__class__.__name__


    def run(self):
        connect()

    
    def connect(self):
        """Open an HTTPS connection to the FourSquare API."""
        connection = httplib.HTTPSConnection(HOST)
        connection.request("GET", URL)
        resp = connection.getresponse()
        connection.connect()
        # Choose the response.
        if resp.status == 200:
            read_response(resp)

        # Close the connection after the reception of data.
        connection.close()

    
    def read_response(response):
        """Get the response from the stream and print it."""
        data = response.read()
        if __debug:
            print data, "\n"
