# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from snyk_python_sdk.paths.groups_group_id_audit_logs_search.get import SearchGroupAuditLogsRaw
from snyk_python_sdk.paths.orgs_org_id_audit_logs_search.get import SearchOrganizationAuditLogsRaw


class AuditLogsApiRaw(
    SearchGroupAuditLogsRaw,
    SearchOrganizationAuditLogsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
