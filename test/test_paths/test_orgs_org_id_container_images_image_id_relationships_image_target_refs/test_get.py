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
from snyk_python_sdk.paths.orgs_org_id_container_images_image_id_relationships_image_target_refs import get
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrgsOrgIdContainerImagesImageIdRelationshipsImageTargetRefs(ApiTestMixin, unittest.TestCase):
    """
    OrgsOrgIdContainerImagesImageIdRelationshipsImageTargetRefs unit test stubs
        List instances of image target references for a container image
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
