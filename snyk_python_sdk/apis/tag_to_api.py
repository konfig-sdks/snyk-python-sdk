import typing_extensions

from snyk_python_sdk.apis.tags import TagValues
from snyk_python_sdk.apis.tags.apps_api import AppsApi
from snyk_python_sdk.apis.tags.service_accounts_api import ServiceAccountsApi
from snyk_python_sdk.apis.tags.collection_api import CollectionApi
from snyk_python_sdk.apis.tags.slack_settings_api import SlackSettingsApi
from snyk_python_sdk.apis.tags.issues_api import IssuesApi
from snyk_python_sdk.apis.tags.custom_base_images_api import CustomBaseImagesApi
from snyk_python_sdk.apis.tags.iac_settings_api import IacSettingsApi
from snyk_python_sdk.apis.tags.orgs_api import OrgsApi
from snyk_python_sdk.apis.tags.projects_api import ProjectsApi
from snyk_python_sdk.apis.tags.container_image_api import ContainerImageApi
from snyk_python_sdk.apis.tags.invites_api import InvitesApi
from snyk_python_sdk.apis.tags.targets_api import TargetsApi
from snyk_python_sdk.apis.tags.audit_logs_api import AuditLogsApi
from snyk_python_sdk.apis.tags.open_api_api import OpenAPIApi
from snyk_python_sdk.apis.tags.sast_settings_api import SastSettingsApi
from snyk_python_sdk.apis.tags.slack_api import SlackApi
from snyk_python_sdk.apis.tags.sbom_api import SBOMApi
from snyk_python_sdk.apis.tags.examples_api import ExamplesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.APPS: AppsApi,
        TagValues.SERVICE_ACCOUNTS: ServiceAccountsApi,
        TagValues.COLLECTION: CollectionApi,
        TagValues.SLACK_SETTINGS: SlackSettingsApi,
        TagValues.ISSUES: IssuesApi,
        TagValues.CUSTOM_BASE_IMAGES: CustomBaseImagesApi,
        TagValues.IAC_SETTINGS: IacSettingsApi,
        TagValues.ORGS: OrgsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.CONTAINER_IMAGE: ContainerImageApi,
        TagValues.INVITES: InvitesApi,
        TagValues.TARGETS: TargetsApi,
        TagValues.AUDIT_LOGS: AuditLogsApi,
        TagValues.OPEN_API: OpenAPIApi,
        TagValues.SAST_SETTINGS: SastSettingsApi,
        TagValues.SLACK: SlackApi,
        TagValues.SBOM: SBOMApi,
        TagValues.EXAMPLES: ExamplesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.APPS: AppsApi,
        TagValues.SERVICE_ACCOUNTS: ServiceAccountsApi,
        TagValues.COLLECTION: CollectionApi,
        TagValues.SLACK_SETTINGS: SlackSettingsApi,
        TagValues.ISSUES: IssuesApi,
        TagValues.CUSTOM_BASE_IMAGES: CustomBaseImagesApi,
        TagValues.IAC_SETTINGS: IacSettingsApi,
        TagValues.ORGS: OrgsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.CONTAINER_IMAGE: ContainerImageApi,
        TagValues.INVITES: InvitesApi,
        TagValues.TARGETS: TargetsApi,
        TagValues.AUDIT_LOGS: AuditLogsApi,
        TagValues.OPEN_API: OpenAPIApi,
        TagValues.SAST_SETTINGS: SastSettingsApi,
        TagValues.SLACK: SlackApi,
        TagValues.SBOM: SBOMApi,
        TagValues.EXAMPLES: ExamplesApi,
    }
)
