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
from snyk_python_sdk.paths.groups_group_id_settings_iac import patch
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestGroupsGroupIdSettingsIac(ApiTestMixin, unittest.TestCase):
    """
    GroupsGroupIdSettingsIac unit test stubs
        Update the Infrastructure as Code Settings for a group
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
