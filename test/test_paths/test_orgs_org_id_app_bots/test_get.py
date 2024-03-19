# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import snyk_python_sdk
from snyk_python_sdk.paths.orgs_org_id_app_bots import get
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrgsOrgIdAppBots(ApiTestMixin, unittest.TestCase):
    """
    OrgsOrgIdAppBots unit test stubs
        Get a list of app bots authorized to an organization.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
