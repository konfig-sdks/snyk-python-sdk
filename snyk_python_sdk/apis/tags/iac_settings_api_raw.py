# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from snyk_python_sdk.paths.groups_group_id_settings_iac.get import GetForGroupRaw
from snyk_python_sdk.paths.orgs_org_id_settings_iac.get import GetForOrgIacRaw
from snyk_python_sdk.paths.groups_group_id_settings_iac.patch import UpdateForGroupRaw
from snyk_python_sdk.paths.orgs_org_id_settings_iac.patch import UpdateForOrgRaw


class IacSettingsApiRaw(
    GetForGroupRaw,
    GetForOrgIacRaw,
    UpdateForGroupRaw,
    UpdateForOrgRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass