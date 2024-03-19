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
from snyk_python_sdk.paths.orgs_org_id_apps_creations_app_id import get
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrgsOrgIdAppsCreationsAppId(ApiTestMixin, unittest.TestCase):
    """
    OrgsOrgIdAppsCreationsAppId unit test stubs
        Get a Snyk App by its App ID.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
