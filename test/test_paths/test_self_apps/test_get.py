# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import snyk_python_sdk
from snyk_python_sdk.paths.self_apps import get
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSelfApps(ApiTestMixin, unittest.TestCase):
    """
    SelfApps unit test stubs
        Get a list of apps that can act on your behalf.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
