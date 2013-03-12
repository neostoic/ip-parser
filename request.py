#!/usr/bin/env python

"""request.py -- Contain the base class for every request."""

from datetime import datetime

class Request(object):
    def __init__(self, host, url, typeOfReq, params=None):
        self.params = params
        self.host = host
        self.typeOfReq = typeOfReq
        if self.params != None:
            self.url = url + '&'.join(["%s=%s" % (k, v) for k, v in self.params.items()])
        else:
            self.url = url
        
    def __unicode__(self):
        return u"<%s: (%s)>" % (self.__class__.__name__, self.args)
        
    def __repr__(self):
        return "<%s: (%s)>" % (self.__class__.__name__, self.args)    
        
    def __str__(self):
        return "<%s: (%s)>" % (self.__class__.__name__, self.args)



## --------------------------------------------------------------------------- ##
## --------------------------------------------------------------------------- ##
## --------------------------------------------------------------------------- ##


# Sanity check...
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
    print r.url, "\n"
    print r.host, r.typeOfReq

    r = Request('api.yelp.com', "/business_review_search?", "GET", {'term': 'yelp', "tl_lat": "37.9", "tl_long": "-122.5", "br_lat": "37.788022", "br_long": "-122.399797", "limit": "3", "ywsid": "WWWW"})
    print r.url, "\n"
    print r.host, r.typeOfReq

    r = Request('api.yelp.com', '/bin', "GET")
    print r.url, "\n"
    print r.host, r.typeOfReq
