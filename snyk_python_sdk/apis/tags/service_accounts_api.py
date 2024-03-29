# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from snyk_python_sdk.paths.orgs_org_id_service_accounts.post import CreateForOrganization
from snyk_python_sdk.paths.groups_group_id_service_accounts.post import CreateGroup
from snyk_python_sdk.paths.groups_group_id_service_accounts_serviceaccount_id.delete import DeleteGroupServiceAccount
from snyk_python_sdk.paths.orgs_org_id_service_accounts_serviceaccount_id.delete import DeleteOrgServiceAccount
from snyk_python_sdk.paths.groups_group_id_service_accounts_serviceaccount_id.get import GetGroupServiceAccount
from snyk_python_sdk.paths.orgs_org_id_service_accounts_serviceaccount_id.get import GetOrganizationAccountById
from snyk_python_sdk.paths.groups_group_id_service_accounts.get import ListGroupServiceAccounts
from snyk_python_sdk.paths.orgs_org_id_service_accounts.get import ListOrganizationServiceAccounts
from snyk_python_sdk.paths.groups_group_id_service_accounts_serviceaccount_id_secrets.post import ManageClientSecret
from snyk_python_sdk.paths.orgs_org_id_service_accounts_serviceaccount_id_secrets.post import ManageClientSecretForOrganizationServiceAccount
from snyk_python_sdk.paths.groups_group_id_service_accounts_serviceaccount_id.patch import UpdateGroupNameById
from snyk_python_sdk.paths.orgs_org_id_service_accounts_serviceaccount_id.patch import UpdateOrganizationServiceAccountName
from snyk_python_sdk.apis.tags.service_accounts_api_raw import ServiceAccountsApiRaw


class ServiceAccountsApi(
    CreateForOrganization,
    CreateGroup,
    DeleteGroupServiceAccount,
    DeleteOrgServiceAccount,
    GetGroupServiceAccount,
    GetOrganizationAccountById,
    ListGroupServiceAccounts,
    ListOrganizationServiceAccounts,
    ManageClientSecret,
    ManageClientSecretForOrganizationServiceAccount,
    UpdateGroupNameById,
    UpdateOrganizationServiceAccountName,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ServiceAccountsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ServiceAccountsApiRaw(api_client)
