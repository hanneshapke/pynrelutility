#!/usr/bin/env python
#
# Hannes Hapke - Santiago, Chile - 2014
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

"""
Unit tests for pynrelutility.

"""

import unittest
import json
from nrel_utility import NRELUtilityWrapper, NRELUtilityResults 

NREL_API_KEY = 'DEMO_KEY' 

MOCK_DATA_NREL_RESPONSE = """
{"inputs":{"address":"2114 Bigelow Ave Seattle, WA, 98109"},"errors":[],"warnings":[],"version":"3.0.3","metadata":{"sources":["Ventyx Research (2011)","EIA (2011)"]},"outputs":{"company_id":"16868","utility_name":"Seattle City Light","utility_info":[{"company_id":"16868","utility_name":"Seattle City Light"}],"commercial":0.0661,"industrial":0.0573,"residential":0.076}}"""


class Test(unittest.TestCase):
    """
    Unit tests for pynrelutility.

    """
    def test_nrel_utility_api_results(self):
        """
        """

        address = '2114 Bigelow Ave Seattle, WA, 98109'

        # create expected result from mock data
        response_mock = json.loads(MOCK_DATA_NREL_RESPONSE)

        # create response from zillow
        nrel_data = NRELUtilityWrapper(NREL_API_KEY)
        response_nrel = nrel_data.get_nrel_utility_data(address)

        # compare expected with real result
        self.assertEqual(json.dumps(response_mock), json.dumps(response_nrel))

    def test_nrel_utility_results(self):
        """
        """

        address = '2114 Bigelow Ave Seattle, WA, 98109'

        nrel_data = NRELUtilityWrapper(NREL_API_KEY)
        nrel_response = nrel_data.get_nrel_utility_data(address)
        result = NRELUtilityResults(nrel_response) 

        self.assertEqual(result.utility_name, 'Seattle City Light')
        self.assertEqual(result.utility_name_list, ['Seattle City Light'])
        self.assertEqual(result.commercial, float('0.0661'))
        self.assertEqual(result.industrial, float('0.0573'))
        self.assertEqual(result.residential, float('0.076'))

if __name__ == "__main__":
    unittest.main()