# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from snyk_python_sdk.paths.groups_group_id_audit_logs_search.get import SearchGroupAuditLogs
from snyk_python_sdk.paths.orgs_org_id_audit_logs_search.get import SearchOrganizationAuditLogs
from snyk_python_sdk.apis.tags.audit_logs_api_raw import AuditLogsApiRaw


class AuditLogsApi(
    SearchGroupAuditLogs,
    SearchOrganizationAuditLogs,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AuditLogsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AuditLogsApiRaw(api_client)