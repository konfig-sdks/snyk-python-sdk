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
from snyk_python_sdk.paths.orgs_org_id_collections_collection_id_relationships_projects import delete
from snyk_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOrgsOrgIdCollectionsCollectionIdRelationshipsProjects(ApiTestMixin, unittest.TestCase):
    """
    OrgsOrgIdCollectionsCollectionIdRelationshipsProjects unit test stubs
        Remove projects from a collection
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()