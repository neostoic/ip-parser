debug = True


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
URL = "/v2/venues/search?ll={latitude},{longitude}&client_id={client_id}&client_secret={client_secret}&v={date}".format(client_id=CLIENT_ID, client_secret=CLIENT_SEC, date=DATE, latitude="35.339879", longitude="25.134591")


if debug:
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
    #if __debug:
    print data, "\n"
    #print_json(data)
