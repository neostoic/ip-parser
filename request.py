#!/usr/bin/env python

"""request.py -- Contain the base class for every request."""

from datetime import datetime

class Request(object):
    def __init__(self, args):
        """Constructor for a request."""
        self.args = args
        self.timestamp = datetime.now()
        
        def args():
            doc = "Accessor methods for the passed arguments. Always give a dictionary with your arguments."
            def fget(self):
                return self.args
            
            def fset(self, args):
                if isinstance(args, dict):
                    self.args = args
                else:
                    raise TypeError("Incorrect type of argument passed.\nYou passed %s, but %s is required" % (args.__class__.__name__, dict.__class__.__name__))

            def fdel(self):
                del self.args
            
            return locals()
            
    def url(self):
        return self.args["url"]
    
    def typeOfReq(self):
        return self.args["typeofreq"]
    
    def host(self):
        return self.args["host"]
        
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
    URL = "/v2/venues/search?ll={lat},{long}&client_id={client_id}&client_secret={client_secret}&v={date}".format(client_id=CLIENT_ID, client_secret=CLIENT_SEC, date=DATE, lat="35.339879", long="25.134591")
    
    r = Request({"host": "api.foursquare.com", "url": URL, "typeofreq": "GET", "client_id": CLIENT_ID, "client_secret": CLIENT_SEC})

    print(r.host())
    print(r.url())
    print(r.typeOfReq())

    URL = 'business_review_search?term=yelp&tl_lat=37.9&tl_long=-122.5&br_lat=37.788022&br_long=-122.399797&limit=3&ywsid=XXXXXXXXXXXXXXXXXX'
    r = Request({'host': 'api.yelp.com', 'url': URL, 'typeofreq': 'GET', 'ywsid': YWSID})
    

