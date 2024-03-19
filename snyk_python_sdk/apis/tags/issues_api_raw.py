# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from snyk_python_sdk.paths.groups_group_id_issues.get import ByGroupIdRaw
from snyk_python_sdk.paths.orgs_org_id_issues_issue_id.get import GetByIdRaw
from snyk_python_sdk.paths.groups_group_id_issues_issue_id.get import GetByIssueIdRaw
from snyk_python_sdk.paths.orgs_org_id_issues.get import ListByOrgIdRaw
from snyk_python_sdk.paths.orgs_org_id_packages_purl_issues.get import ListByPackageRaw
from snyk_python_sdk.paths.orgs_org_id_packages_issues.post import QueryForPackagesRaw


class IssuesApiRaw(
    ByGroupIdRaw,
    GetByIdRaw,
    GetByIssueIdRaw,
    ListByOrgIdRaw,
    ListByPackageRaw,
    QueryForPackagesRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
