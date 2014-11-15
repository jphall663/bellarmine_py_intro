#!/usr/bin/env python

"""

Sample program to query the Yelp API.

jpatrickhall@gmail.com

Requirements:

1.) Open your Anaconda terminal. From your Anaconda terminal, install
the OAuth open authentication library with the commands:
pip install httplib2
pip install oauth2

2.) You must have a Yelp account. If you don't, sign up for one at:
http://www.yelp.com/developers ---> Getting Started

3.) Once you can sign into Yelp, follow the instructions for recieving
an API key under the getting started tab:
http://www.yelp.com/developers ---> Getting Started

Your website is:
http://www.bellarmine.edu/analytics/

Your industry is:
Other --> Education

4.) Record your key information below.

5.) To execute from Anaconda terminal:

python C:/Path/to/yelp_api_example.py
"""

### AUTHENTICATION INFORMATION
# INSERT YOUR OWN INFORMATION

CONSUMER_KEY = 'ZNSkhQMLWqQUsZzx1Upy9g'
CONSUMER_SECRET = '5f67FFCIjqSVjHg-uyN203P9r2I'
TOKEN = 'Yn3NkYrjs7D15m7XtcWZBtCqXylZ-fd9'
TOKEN_SECRET = '92yHDv6SymFiOtKEvtSt3cHjuVY'

### QUERY INFORMATION
# YOU CAN ATTEMPT TO CHANGE THESE
# TERMS LIKE: dinner AND restaurant WORK WELL
# LOCATIONS ARE SEPARATED BY COMMAS
# SEARCH_LIMIT <= 20
# REMEMBER YOU MAY BE LIMITED TO A CERTAIN NUMBER OF
#   SEARCHES (SEARCH_LIMIT) PER DAY
# YOU MAY ATTEMPT TO ADD MORE FIELDS TO YOUR OUTPUT
#   BUT THE CODE AS WRITTEN IS ONLY VALID FOR NON-NESTED
#   DICTIONARY ELEMENTS

TERM = 'dinner'
LOCATION = 'Louisville, KY'
SEARCH_LIMIT = 20
DESIRED_FIELDS = ['rating', 'review_count', 'name', 'url', 'is_closed',\
                  'snippet_text']

### DO NOT CHANGE BELOW ###################################

API_HOST = 'api.yelp.com'
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

import csv
import datetime
import json
import oauth2
import sys
import time
import urllib2

### DO NOT CHANGE ABOVE ###################################

def write_output(businesses, term, location):

    """Writes CSV output of query results.

    Args:
        businesses (dict): The businesses returned by the query.
        term (str): Query search term specified by user.
        location (str): Query search location specified by user.

    Raises:
        IOError: if output file is inaccessible.
        LookupError: if a record if incomplete.
    """

    ### CREATE TIME STAMPED OUTPUT FILE NAME
    time_stamp = datetime.datetime.fromtimestamp(time.time())\
        .strftime('%Y-%m-%d_%H-%M-%S')
    outfile_name = '{0}_{1}_{2}.csv'.format(term.replace(' ', '-')\
        .replace(',', '-'), location.replace(' ', '-').replace(',', '-'),\
        time_stamp)
    ofile_ref = open(outfile_name, 'a+')
    csv_writer = csv.writer(ofile_ref)

    ### TAKE VAR NAMES FROM INTERSECTION OF DESIRED_FIELDS
    ###   AND FIELDS AVAILABLE IN FIRST RETURNED BUSINESS
    csv_writer.writerow([field.encode('ascii', 'ignore') for field in\
        businesses[0].keys() if field in DESIRED_FIELDS])

    ### WRITE DATA ROWS
    count = 0
    for i in range(0, len(businesses)):
        try:
            business_id = businesses[i]['id']
            print 'Parsing result for business "{0}" ...'.format(business_id)
            count += 1
            csv_writer.writerow(\
                [str(businesses[i][key]).encode('ascii', 'ignore') \
                for key in businesses[i].keys() if key.encode('ascii',\
                'ignore') in DESIRED_FIELDS])
        except IOError as exception:
            print 'Cannot access output file.'
            print exception.message()
            sys.exit(-1)
        except LookupError:
            print 'Record not retrieved for index {0}'.format(str(i))
            continue

    print 'Information for {0} total businesses written.'.format(count)

    ofile_ref.close()

def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """

    ### AUTHENTICATION
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, path)
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request('GET', url=url, parameters=url_params)
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer,\
                               token)
    signed_url = oauth_request.to_url()

    ### QUERY
    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

def query_api(term, location):
    """Begins constructing queries to the API by the input values from
       the user and validates query response.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """

    ### PREPARE TERMS TO BE PLACED IN API URL
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }

    ### DETERMINE IF BUSINESSES WERE FOUND BY YOUR QUERY
    response = request(API_HOST, SEARCH_PATH, url_params=url_params)
    businesses = response.get('businesses')

    ### IF NO, EXIT
    ### IF YES, PARSE JSON INTO CSV
    if not businesses:
        print 'No businesses for {0} in {1} found.'.format(term, location)
        return
    else:
        print '{0} businesses found, parsing business info ...'\
            .format(len(businesses))
        write_output(businesses, term, location)

### EXECUTE
def main():
    """ Run as standalone script """

    try:
        query_api(TERM, LOCATION)
    except urllib2.HTTPError as error:
        sys.exit('Encountered HTTP error {0}. Abort program.'\
            .format(error.code))

if __name__ == '__main__':
    main()











