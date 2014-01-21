import requests
import sys
from requests.exceptions import (ConnectionError, TooManyRedirects, 
                                Timeout, HTTPError)

try:
    import json
except ImportError:
    import simplejson as json


from nrel_utility_errors import NRELFail, NRELNoResults
from __version__ import VERSION


class NRELUtilityWrapper(object):
    """
    """

    def __init__(self, api_key='DEMO_KEY'):
        """

        """
        self.api_key = api_key

    def get_nrel_utility_data(self, address):
        """
        NREL Utility API
        """

        url = 'http://developer.nrel.gov/api/utility_rates/v3.json'
        params = {
            'format': 'json',
            'address': address,
            'api_key': self.api_key 
            }
        return self.get_data(url, params)

    def get_data(self, url, params):
        """
        """

        try:
            request = requests.get(
                url = url,
                params = params,
                headers = {
                    'User-Agent': 'NREL Utility Wrapper/' + VERSION + ' (Python)'
                })
            print request.url
        except (ConnectionError, TooManyRedirects, Timeout):
            raise NRELFail

        try:
            request.raise_for_status()
        except HTTPError:
            raise NRELFail

        try:
            response_json = request.json()
        except ValueError:
            print "NREL utility data is not a valid json structure" # (%s)" % (params['address'])
            raise NRELFail

        if not response_json:
            print "NREL utility API did not return any results" # (%s)" % (params['address'])
            raise NRELNoResults

        if response_json['errors']:
            raise NRELError(response_json['errors'])
        else:
            return response_json


class NRELUtilityResults(object):
    """
    """

    attribute_mapping = {}

    def __init__(self, data):
        """
        Creates instance of GeocoderResult from the provided JSON data array
        """
        print data
        self.data = data
        self.len = len(self.data)
        self.current_data = self.data

    def __len__(self):
        return self.len

    def __iter__(self):
        return self

    def return_next(self):
        if self.current_index >= self.len:
            raise StopIteration
        self.current_data = self.data[self.current_index]
        self.current_index += 1
        return self

    def __unicode__(self):
        return self.zillow_id

    if sys.version_info[0] >= 3:  # Python 3
        def __str__(self):
            return self.__unicode__()

        def __next__(self):
            return self.return_next()
    else:  # Python 2
        def __str__(self):
            return self.__unicode__().encode('utf8')

        def next(self):
            return self.return_next()

    @property
    def count(self):
        return self.len

    @property
    def utility_name(self):
        """
        Returns the name of the utilities 
        (From NREL: If there are multiple utility companies serving the 
        location, the names will be returned as a pipe-delimited string.)
        """
        return self.current_data['outputs']['utility_name']

    @property
    def utility_name_list(self):
        """
        Returns the name of the utilities as a python list
        """
        utility_list = []
        json_attribute = self.current_data['outputs']['utility_info']

        for item in json_attribute:
            utility_list.append(item['utility_name'])
        return utility_list

    @property
    def residential(self):
        """
        """
        return self.current_data['outputs']['residential']

    @property
    def commercial(self):
        """
        
        """
        return self.current_data['outputs']['commercial']

    @property
    def industrial(self):
        """
        
        """
        return self.current_data['outputs']['industrial']



