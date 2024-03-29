# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from snyk_python_sdk.paths.orgs_org_id.get import GetDetails
from snyk_python_sdk.paths.orgs.get import ListAccessibleOrganizations
from snyk_python_sdk.paths.groups_group_id_orgs.get import ListGroupOrgs
from snyk_python_sdk.paths.orgs_org_id.patch import UpdateDetails
from snyk_python_sdk.apis.tags.orgs_api_raw import OrgsApiRaw


class OrgsApi(
    GetDetails,
    ListAccessibleOrganizations,
    ListGroupOrgs,
    UpdateDetails,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OrgsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OrgsApiRaw(api_client)
