#!/usr/bin/env python

"""parser.py -- A parser for FourSquare data."""


__author__ = "ipinak"
__version__ = "0.1"
__copyright__ = "No copyright yet"

debug = True


try:
    import threading
    import httplib
    import json
    from request import Request
    from datetime import datetime
except ImportError as e:
    print("Some of your import does not exist")
    print("[Error occurred: %d - %s]" % (e.errno, e.strerror))


class BaseConnector(threading.Thread):
    """
    Base connector class to make a request to various APIs and retrieve
    data.
    """
    def __init__(self, request, callback=None):
        if debug: print('%s.__init__()' % (self.__class__.__name__))
        assert request.__class__.__name__ != Request.__class__.__name__
        self.callback = callback
        self.request = request
        threading.Thread.__init__(self)
        
        def request():
            doc = 'information about the request you want to make'
            
            def fget(self):
                return self._request
            
            def fset(self, request):
                self._request = request
            
            def fdel(self):
                del self._request
            
            return locals()
        
    def __str__(self):
        return self.__class__.__name__

    def __unicode__(self):
        return self.__class__.__name__
    
    def run(self):
        """Open an HTTPS connection to the FourSquare API."""
        connection = httplib.HTTPSConnection(self.request.host)
        connection.request(self.request.typeOfReq, self.request.url)

        try:
            resp = connection.getresponse()
            connection.connect()
        except httplib.HTTPException:
            print("HTTPException")
        except httplib.NotConnected:
            print("Not Connected")
        except httplib.CannotSendRequest:
            print("Cannot send request")
        except httplib.ResponseNotReady:
            print("ResponseNotReady")
        except httplib.CannoSendHeader:
            print("Cannot Send Header")
        except httplib.IncompleteRead:
            print("Incoplete Read")
        else:
            print("Something else happened")
        finally:
            print("Finally closed.")
            
        # Choose the response.
        if resp.status == 200:
            if self.callback == None:
                self.read_response(resp)
            else:
                self.callback(resp)

        # Close the connection after the reception of data.
        connection.close()
        
    def read_response(self, response):
        """Get the response from the stream and print it."""
        data = response.read()
        if debug:
            print(data, "\n")


class YelpConnector(BaseConnector):
    """
    Class to make a request to Yelp API and retrieve data.
    """
    def __init__(self, request, callback=None):
        BaseConnector.__init__(self, request, callback)
    
    def __str__(self):
        return self.__class__.__name__
    
    def __unicode(self):
        return self.__class__.__name__

    def run(self):
        BaseConnector.run(self)
    
    def read_response(self, response):
        BaseConnector.read_response(self, response)
        
        
class FSQConnector(BaseConnector):
    """
    Class to make a request to FourSquare API and retrieve
    data.
    """
    def __init__(self, request, callback=None):
        BaseConnector.__init__(self, request, callback)
    
    def __str__(self):
        return self.__class__.__name__
    
    def __unicode(self):
        return self.__class__.__name__

    def run(self):
        BaseConnector.run(self)
    
    def read_response(self, response):
        BaseConnector.read_response(self, response)


class GoogleConnector(BaseConnector):
    """
    Class to make a request to Google API and retrieve
    data.
    """
    def __init__(self, request, callback=None):
        BaseConnector.__init__(self, request, callback)
    
    def __str__(self):
        return self.__class__.__name__
    
    def __unicode(self):
        return self.__class__.__name__

    def run(self):
        BaseConnector.run(self)
    
    def read_response(self, response):
        BaseConnector.read_response(self, response)


class Parser(threading.Thread):
    def __init__(self, data, callback):
        self._data = data
        self.callback = callback
        threading.Thread.__init__(self)
        
        def data():
            doc = "Read-only access for the data."
            
            def fget(self):
                return self._data
            
            def fdel(self):
                del self._data
                
            return locals()
    
    def __unicode__(self):
        return u"<%s: %s>" % (self.__class__.__name__, self._func)
    
    def run(self):
        retVal = json.loads(self._data, sort_keys=True)
        try:
            self.callback(retVal)
        except TypeError, e:
            print("Error: %d - %s" % (e.errno, r.strerror))


###############################################################################


if __name__ == "__main__":
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
    r = Request("api.foursquare.com", "/v2/venues/search?", "GET", {"ll": "35.33879,25.134591", "client_id": CLIENT_ID, "client_secret": CLIENT_SEC, "v": DATE})
    connector = FSQConnector(r)
    #connector = BaseConnector(r)
    connector.start()

    # Create a userless url, using the client id, the client secret 
    # and the current date in the specified format.
    # More about userless: http://www.yelp.com/developers/documentation/search_api#sampleResponse
    r = Request('api.yelp.com', "/business_review_search?", "GET", {'term': 'yelp', "tl_lat": "37.9", "tl_long": "-122.5", "br_lat": "37.788022", "br_long": "-122.399797", "limit": "3", "ywsid": "WWWW"})
    print r.url, r.host, r.typeOfReq
    
    connector = YelpConnector(r)
    connector.start()
    
    # URL = "/maps/api/service/output?"
    # r = Request("maps.googleapis.com", URL, "GET")
    # connector = GoogleConnector(r)
    # connector.start()
    
