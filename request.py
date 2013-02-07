#!/usr/bin/env python

"""request.py -- Contain the base class for every request."""

class Request(object):
    def __init__(self, url, host, args):
        """Creation method for a FourSquare request."""
        self.url = url
        self.host = u"api.foursquare.com"
        self.args = args
        
        def url():
            doc = "Accessor methods for the url attribute."
            def fget(self):
                return self._url
            
            def fset(self, url):
                self._url = url
            
            def fdel(self):
                del self._url
            
            return locals()
        
        def args():
            doc = "Accessor methods for the passed arguments."
            def fget(self):
                return self._args
            
            def fset(self, args):
                self._args = args

            def fdel(self):
                del self._args
            
            return locals()


        def __unicode__(self):
            return u"<%s: (%s, %s, %s)>" % (self.__class__.__name__, self._url, self._host, self._args)

        
        def __repr__(self):
            return u"<%s: (%s, %s, %s)>" % (self.__class__.__name__, self._url, self._host, self._args)
        
        
        def __str__(self):
            return u"<%s: (%s, %s, %s)>" % (self.__class__.__name__, self._url, self._host, self._args)



# Sanity check...
if __name__ == "__main__":
    r = Request("test_url", "host", {"h": 1})
    print r.url
    print r.host
    print r.args
    print r
