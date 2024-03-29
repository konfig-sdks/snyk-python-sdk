# coding: utf-8
"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from snyk_python_sdk.client_custom import ClientCustom
from snyk_python_sdk.configuration import Configuration
from snyk_python_sdk.api_client import ApiClient
from snyk_python_sdk.type_util import copy_signature
from snyk_python_sdk.apis.tags.apps_api import AppsApi
from snyk_python_sdk.apis.tags.audit_logs_api import AuditLogsApi
from snyk_python_sdk.apis.tags.collection_api import CollectionApi
from snyk_python_sdk.apis.tags.container_image_api import ContainerImageApi
from snyk_python_sdk.apis.tags.custom_base_images_api import CustomBaseImagesApi
from snyk_python_sdk.apis.tags.iac_settings_api import IacSettingsApi
from snyk_python_sdk.apis.tags.invites_api import InvitesApi
from snyk_python_sdk.apis.tags.issues_api import IssuesApi
from snyk_python_sdk.apis.tags.open_api_api import OpenAPIApi
from snyk_python_sdk.apis.tags.orgs_api import OrgsApi
from snyk_python_sdk.apis.tags.projects_api import ProjectsApi
from snyk_python_sdk.apis.tags.sbom_api import SBOMApi
from snyk_python_sdk.apis.tags.sast_settings_api import SastSettingsApi
from snyk_python_sdk.apis.tags.service_accounts_api import ServiceAccountsApi
from snyk_python_sdk.apis.tags.slack_api import SlackApi
from snyk_python_sdk.apis.tags.slack_settings_api import SlackSettingsApi
from snyk_python_sdk.apis.tags.targets_api import TargetsApi



class Snyk(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.apps: AppsApi = AppsApi(api_client)
        self.audit_logs: AuditLogsApi = AuditLogsApi(api_client)
        self.collection: CollectionApi = CollectionApi(api_client)
        self.container_image: ContainerImageApi = ContainerImageApi(api_client)
        self.custom_base_images: CustomBaseImagesApi = CustomBaseImagesApi(api_client)
        self.iac_settings: IacSettingsApi = IacSettingsApi(api_client)
        self.invites: InvitesApi = InvitesApi(api_client)
        self.issues: IssuesApi = IssuesApi(api_client)
        self.open_api: OpenAPIApi = OpenAPIApi(api_client)
        self.orgs: OrgsApi = OrgsApi(api_client)
        self.projects: ProjectsApi = ProjectsApi(api_client)
        self.sbom: SBOMApi = SBOMApi(api_client)
        self.sast_settings: SastSettingsApi = SastSettingsApi(api_client)
        self.service_accounts: ServiceAccountsApi = ServiceAccountsApi(api_client)
        self.slack: SlackApi = SlackApi(api_client)
        self.slack_settings: SlackSettingsApi = SlackSettingsApi(api_client)
        self.targets: TargetsApi = TargetsApi(api_client)
