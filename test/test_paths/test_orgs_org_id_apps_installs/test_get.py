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
from snyk_python_sdk.paths.orgs_org_id_apps_installs import get
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrgsOrgIdAppsInstalls(ApiTestMixin, unittest.TestCase):
    """
    OrgsOrgIdAppsInstalls unit test stubs
        Get a list of apps installed for an organization.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()