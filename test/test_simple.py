# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from snyk_python_sdk import Snyk

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        snyk = Snyk(
        
                        api_token = 'YOUR_API_KEY',
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(snyk)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()