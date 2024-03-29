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
from snyk_python_sdk.paths.custom_base_images import post
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCustomBaseImages(ApiTestMixin, unittest.TestCase):
    """
    CustomBaseImages unit test stubs
        Create a Custom Base Image from an existing container project
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
