import typing_extensions

from snyk_python_sdk.paths import PathValues
from snyk_python_sdk.apis.paths.custom_base_images import CustomBaseImages
from snyk_python_sdk.apis.paths.custom_base_images_custombaseimage_id import CustomBaseImagesCustombaseimageId
from snyk_python_sdk.apis.paths.groups_group_id_apps_installs import GroupsGroupIdAppsInstalls
from snyk_python_sdk.apis.paths.groups_group_id_apps_installs_install_id import GroupsGroupIdAppsInstallsInstallId
from snyk_python_sdk.apis.paths.groups_group_id_apps_installs_install_id_secrets import GroupsGroupIdAppsInstallsInstallIdSecrets
from snyk_python_sdk.apis.paths.groups_group_id_audit_logs_search import GroupsGroupIdAuditLogsSearch
from snyk_python_sdk.apis.paths.groups_group_id_issues import GroupsGroupIdIssues
from snyk_python_sdk.apis.paths.groups_group_id_issues_issue_id import GroupsGroupIdIssuesIssueId
from snyk_python_sdk.apis.paths.groups_group_id_orgs import GroupsGroupIdOrgs
from snyk_python_sdk.apis.paths.groups_group_id_service_accounts import GroupsGroupIdServiceAccounts
from snyk_python_sdk.apis.paths.groups_group_id_service_accounts_serviceaccount_id import GroupsGroupIdServiceAccountsServiceaccountId
from snyk_python_sdk.apis.paths.groups_group_id_service_accounts_serviceaccount_id_secrets import GroupsGroupIdServiceAccountsServiceaccountIdSecrets
from snyk_python_sdk.apis.paths.groups_group_id_settings_iac import GroupsGroupIdSettingsIac
from snyk_python_sdk.apis.paths.openapi import Openapi
from snyk_python_sdk.apis.paths.openapi_version import OpenapiVersion
from snyk_python_sdk.apis.paths.orgs import Orgs
from snyk_python_sdk.apis.paths.orgs_org_id import OrgsOrgId
from snyk_python_sdk.apis.paths.orgs_org_id_app_bots import OrgsOrgIdAppBots
from snyk_python_sdk.apis.paths.orgs_org_id_app_bots_bot_id import OrgsOrgIdAppBotsBotId
from snyk_python_sdk.apis.paths.orgs_org_id_apps import OrgsOrgIdApps
from snyk_python_sdk.apis.paths.orgs_org_id_apps_creations import OrgsOrgIdAppsCreations
from snyk_python_sdk.apis.paths.orgs_org_id_apps_creations_app_id import OrgsOrgIdAppsCreationsAppId
from snyk_python_sdk.apis.paths.orgs_org_id_apps_creations_app_id_secrets import OrgsOrgIdAppsCreationsAppIdSecrets
from snyk_python_sdk.apis.paths.orgs_org_id_apps_installs import OrgsOrgIdAppsInstalls
from snyk_python_sdk.apis.paths.orgs_org_id_apps_installs_install_id import OrgsOrgIdAppsInstallsInstallId
from snyk_python_sdk.apis.paths.orgs_org_id_apps_installs_install_id_secrets import OrgsOrgIdAppsInstallsInstallIdSecrets
from snyk_python_sdk.apis.paths.orgs_org_id_apps_client_id import OrgsOrgIdAppsClientId
from snyk_python_sdk.apis.paths.orgs_org_id_apps_client_id_secrets import OrgsOrgIdAppsClientIdSecrets
from snyk_python_sdk.apis.paths.orgs_org_id_audit_logs_search import OrgsOrgIdAuditLogsSearch
from snyk_python_sdk.apis.paths.orgs_org_id_collections import OrgsOrgIdCollections
from snyk_python_sdk.apis.paths.orgs_org_id_collections_collection_id import OrgsOrgIdCollectionsCollectionId
from snyk_python_sdk.apis.paths.orgs_org_id_collections_collection_id_relationships_projects import OrgsOrgIdCollectionsCollectionIdRelationshipsProjects
from snyk_python_sdk.apis.paths.orgs_org_id_container_images import OrgsOrgIdContainerImages
from snyk_python_sdk.apis.paths.orgs_org_id_container_images_image_id import OrgsOrgIdContainerImagesImageId
from snyk_python_sdk.apis.paths.orgs_org_id_container_images_image_id_relationships_image_target_refs import OrgsOrgIdContainerImagesImageIdRelationshipsImageTargetRefs
from snyk_python_sdk.apis.paths.orgs_org_id_invites import OrgsOrgIdInvites
from snyk_python_sdk.apis.paths.orgs_org_id_invites_invite_id import OrgsOrgIdInvitesInviteId
from snyk_python_sdk.apis.paths.orgs_org_id_issues import OrgsOrgIdIssues
from snyk_python_sdk.apis.paths.orgs_org_id_issues_issue_id import OrgsOrgIdIssuesIssueId
from snyk_python_sdk.apis.paths.orgs_org_id_packages_issues import OrgsOrgIdPackagesIssues
from snyk_python_sdk.apis.paths.orgs_org_id_packages_purl_issues import OrgsOrgIdPackagesPurlIssues
from snyk_python_sdk.apis.paths.orgs_org_id_projects import OrgsOrgIdProjects
from snyk_python_sdk.apis.paths.orgs_org_id_projects_project_id import OrgsOrgIdProjectsProjectId
from snyk_python_sdk.apis.paths.orgs_org_id_projects_project_id_sbom import OrgsOrgIdProjectsProjectIdSbom
from snyk_python_sdk.apis.paths.orgs_org_id_service_accounts import OrgsOrgIdServiceAccounts
from snyk_python_sdk.apis.paths.orgs_org_id_service_accounts_serviceaccount_id import OrgsOrgIdServiceAccountsServiceaccountId
from snyk_python_sdk.apis.paths.orgs_org_id_service_accounts_serviceaccount_id_secrets import OrgsOrgIdServiceAccountsServiceaccountIdSecrets
from snyk_python_sdk.apis.paths.orgs_org_id_settings_iac import OrgsOrgIdSettingsIac
from snyk_python_sdk.apis.paths.orgs_org_id_settings_sast import OrgsOrgIdSettingsSast
from snyk_python_sdk.apis.paths.orgs_org_id_slack_app_bot_id import OrgsOrgIdSlackAppBotId
from snyk_python_sdk.apis.paths.orgs_org_id_slack_app_bot_id_projects import OrgsOrgIdSlackAppBotIdProjects
from snyk_python_sdk.apis.paths.orgs_org_id_slack_app_bot_id_projects_project_id import OrgsOrgIdSlackAppBotIdProjectsProjectId
from snyk_python_sdk.apis.paths.orgs_org_id_slack_app_tenant_id_channels import OrgsOrgIdSlackAppTenantIdChannels
from snyk_python_sdk.apis.paths.orgs_org_id_slack_app_tenant_id_channels_channel_id import OrgsOrgIdSlackAppTenantIdChannelsChannelId
from snyk_python_sdk.apis.paths.orgs_org_id_targets import OrgsOrgIdTargets
from snyk_python_sdk.apis.paths.orgs_org_id_targets_target_id import OrgsOrgIdTargetsTargetId
from snyk_python_sdk.apis.paths.self_apps import SelfApps
from snyk_python_sdk.apis.paths.self_apps_installs import SelfAppsInstalls
from snyk_python_sdk.apis.paths.self_apps_installs_install_id import SelfAppsInstallsInstallId
from snyk_python_sdk.apis.paths.self_apps_app_id import SelfAppsAppId
from snyk_python_sdk.apis.paths.self_apps_app_id_sessions import SelfAppsAppIdSessions
from snyk_python_sdk.apis.paths.self_apps_app_id_sessions_session_id import SelfAppsAppIdSessionsSessionId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CUSTOM_BASE_IMAGES: CustomBaseImages,
        PathValues.CUSTOM_BASE_IMAGES_CUSTOMBASEIMAGE_ID: CustomBaseImagesCustombaseimageId,
        PathValues.GROUPS_GROUP_ID_APPS_INSTALLS: GroupsGroupIdAppsInstalls,
        PathValues.GROUPS_GROUP_ID_APPS_INSTALLS_INSTALL_ID: GroupsGroupIdAppsInstallsInstallId,
        PathValues.GROUPS_GROUP_ID_APPS_INSTALLS_INSTALL_ID_SECRETS: GroupsGroupIdAppsInstallsInstallIdSecrets,
        PathValues.GROUPS_GROUP_ID_AUDIT_LOGS_SEARCH: GroupsGroupIdAuditLogsSearch,
        PathValues.GROUPS_GROUP_ID_ISSUES: GroupsGroupIdIssues,
        PathValues.GROUPS_GROUP_ID_ISSUES_ISSUE_ID: GroupsGroupIdIssuesIssueId,
        PathValues.GROUPS_GROUP_ID_ORGS: GroupsGroupIdOrgs,
        PathValues.GROUPS_GROUP_ID_SERVICE_ACCOUNTS: GroupsGroupIdServiceAccounts,
        PathValues.GROUPS_GROUP_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID: GroupsGroupIdServiceAccountsServiceaccountId,
        PathValues.GROUPS_GROUP_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID_SECRETS: GroupsGroupIdServiceAccountsServiceaccountIdSecrets,
        PathValues.GROUPS_GROUP_ID_SETTINGS_IAC: GroupsGroupIdSettingsIac,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_VERSION: OpenapiVersion,
        PathValues.ORGS: Orgs,
        PathValues.ORGS_ORG_ID: OrgsOrgId,
        PathValues.ORGS_ORG_ID_APP_BOTS: OrgsOrgIdAppBots,
        PathValues.ORGS_ORG_ID_APP_BOTS_BOT_ID: OrgsOrgIdAppBotsBotId,
        PathValues.ORGS_ORG_ID_APPS: OrgsOrgIdApps,
        PathValues.ORGS_ORG_ID_APPS_CREATIONS: OrgsOrgIdAppsCreations,
        PathValues.ORGS_ORG_ID_APPS_CREATIONS_APP_ID: OrgsOrgIdAppsCreationsAppId,
        PathValues.ORGS_ORG_ID_APPS_CREATIONS_APP_ID_SECRETS: OrgsOrgIdAppsCreationsAppIdSecrets,
        PathValues.ORGS_ORG_ID_APPS_INSTALLS: OrgsOrgIdAppsInstalls,
        PathValues.ORGS_ORG_ID_APPS_INSTALLS_INSTALL_ID: OrgsOrgIdAppsInstallsInstallId,
        PathValues.ORGS_ORG_ID_APPS_INSTALLS_INSTALL_ID_SECRETS: OrgsOrgIdAppsInstallsInstallIdSecrets,
        PathValues.ORGS_ORG_ID_APPS_CLIENT_ID: OrgsOrgIdAppsClientId,
        PathValues.ORGS_ORG_ID_APPS_CLIENT_ID_SECRETS: OrgsOrgIdAppsClientIdSecrets,
        PathValues.ORGS_ORG_ID_AUDIT_LOGS_SEARCH: OrgsOrgIdAuditLogsSearch,
        PathValues.ORGS_ORG_ID_COLLECTIONS: OrgsOrgIdCollections,
        PathValues.ORGS_ORG_ID_COLLECTIONS_COLLECTION_ID: OrgsOrgIdCollectionsCollectionId,
        PathValues.ORGS_ORG_ID_COLLECTIONS_COLLECTION_ID_RELATIONSHIPS_PROJECTS: OrgsOrgIdCollectionsCollectionIdRelationshipsProjects,
        PathValues.ORGS_ORG_ID_CONTAINER_IMAGES: OrgsOrgIdContainerImages,
        PathValues.ORGS_ORG_ID_CONTAINER_IMAGES_IMAGE_ID: OrgsOrgIdContainerImagesImageId,
        PathValues.ORGS_ORG_ID_CONTAINER_IMAGES_IMAGE_ID_RELATIONSHIPS_IMAGE_TARGET_REFS: OrgsOrgIdContainerImagesImageIdRelationshipsImageTargetRefs,
        PathValues.ORGS_ORG_ID_INVITES: OrgsOrgIdInvites,
        PathValues.ORGS_ORG_ID_INVITES_INVITE_ID: OrgsOrgIdInvitesInviteId,
        PathValues.ORGS_ORG_ID_ISSUES: OrgsOrgIdIssues,
        PathValues.ORGS_ORG_ID_ISSUES_ISSUE_ID: OrgsOrgIdIssuesIssueId,
        PathValues.ORGS_ORG_ID_PACKAGES_ISSUES: OrgsOrgIdPackagesIssues,
        PathValues.ORGS_ORG_ID_PACKAGES_PURL_ISSUES: OrgsOrgIdPackagesPurlIssues,
        PathValues.ORGS_ORG_ID_PROJECTS: OrgsOrgIdProjects,
        PathValues.ORGS_ORG_ID_PROJECTS_PROJECT_ID: OrgsOrgIdProjectsProjectId,
        PathValues.ORGS_ORG_ID_PROJECTS_PROJECT_ID_SBOM: OrgsOrgIdProjectsProjectIdSbom,
        PathValues.ORGS_ORG_ID_SERVICE_ACCOUNTS: OrgsOrgIdServiceAccounts,
        PathValues.ORGS_ORG_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID: OrgsOrgIdServiceAccountsServiceaccountId,
        PathValues.ORGS_ORG_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID_SECRETS: OrgsOrgIdServiceAccountsServiceaccountIdSecrets,
        PathValues.ORGS_ORG_ID_SETTINGS_IAC: OrgsOrgIdSettingsIac,
        PathValues.ORGS_ORG_ID_SETTINGS_SAST: OrgsOrgIdSettingsSast,
        PathValues.ORGS_ORG_ID_SLACK_APP_BOT_ID: OrgsOrgIdSlackAppBotId,
        PathValues.ORGS_ORG_ID_SLACK_APP_BOT_ID_PROJECTS: OrgsOrgIdSlackAppBotIdProjects,
        PathValues.ORGS_ORG_ID_SLACK_APP_BOT_ID_PROJECTS_PROJECT_ID: OrgsOrgIdSlackAppBotIdProjectsProjectId,
        PathValues.ORGS_ORG_ID_SLACK_APP_TENANT_ID_CHANNELS: OrgsOrgIdSlackAppTenantIdChannels,
        PathValues.ORGS_ORG_ID_SLACK_APP_TENANT_ID_CHANNELS_CHANNEL_ID: OrgsOrgIdSlackAppTenantIdChannelsChannelId,
        PathValues.ORGS_ORG_ID_TARGETS: OrgsOrgIdTargets,
        PathValues.ORGS_ORG_ID_TARGETS_TARGET_ID: OrgsOrgIdTargetsTargetId,
        PathValues.SELF_APPS: SelfApps,
        PathValues.SELF_APPS_INSTALLS: SelfAppsInstalls,
        PathValues.SELF_APPS_INSTALLS_INSTALL_ID: SelfAppsInstallsInstallId,
        PathValues.SELF_APPS_APP_ID: SelfAppsAppId,
        PathValues.SELF_APPS_APP_ID_SESSIONS: SelfAppsAppIdSessions,
        PathValues.SELF_APPS_APP_ID_SESSIONS_SESSION_ID: SelfAppsAppIdSessionsSessionId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CUSTOM_BASE_IMAGES: CustomBaseImages,
        PathValues.CUSTOM_BASE_IMAGES_CUSTOMBASEIMAGE_ID: CustomBaseImagesCustombaseimageId,
        PathValues.GROUPS_GROUP_ID_APPS_INSTALLS: GroupsGroupIdAppsInstalls,
        PathValues.GROUPS_GROUP_ID_APPS_INSTALLS_INSTALL_ID: GroupsGroupIdAppsInstallsInstallId,
        PathValues.GROUPS_GROUP_ID_APPS_INSTALLS_INSTALL_ID_SECRETS: GroupsGroupIdAppsInstallsInstallIdSecrets,
        PathValues.GROUPS_GROUP_ID_AUDIT_LOGS_SEARCH: GroupsGroupIdAuditLogsSearch,
        PathValues.GROUPS_GROUP_ID_ISSUES: GroupsGroupIdIssues,
        PathValues.GROUPS_GROUP_ID_ISSUES_ISSUE_ID: GroupsGroupIdIssuesIssueId,
        PathValues.GROUPS_GROUP_ID_ORGS: GroupsGroupIdOrgs,
        PathValues.GROUPS_GROUP_ID_SERVICE_ACCOUNTS: GroupsGroupIdServiceAccounts,
        PathValues.GROUPS_GROUP_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID: GroupsGroupIdServiceAccountsServiceaccountId,
        PathValues.GROUPS_GROUP_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID_SECRETS: GroupsGroupIdServiceAccountsServiceaccountIdSecrets,
        PathValues.GROUPS_GROUP_ID_SETTINGS_IAC: GroupsGroupIdSettingsIac,
        PathValues.OPENAPI: Openapi,
        PathValues.OPENAPI_VERSION: OpenapiVersion,
        PathValues.ORGS: Orgs,
        PathValues.ORGS_ORG_ID: OrgsOrgId,
        PathValues.ORGS_ORG_ID_APP_BOTS: OrgsOrgIdAppBots,
        PathValues.ORGS_ORG_ID_APP_BOTS_BOT_ID: OrgsOrgIdAppBotsBotId,
        PathValues.ORGS_ORG_ID_APPS: OrgsOrgIdApps,
        PathValues.ORGS_ORG_ID_APPS_CREATIONS: OrgsOrgIdAppsCreations,
        PathValues.ORGS_ORG_ID_APPS_CREATIONS_APP_ID: OrgsOrgIdAppsCreationsAppId,
        PathValues.ORGS_ORG_ID_APPS_CREATIONS_APP_ID_SECRETS: OrgsOrgIdAppsCreationsAppIdSecrets,
        PathValues.ORGS_ORG_ID_APPS_INSTALLS: OrgsOrgIdAppsInstalls,
        PathValues.ORGS_ORG_ID_APPS_INSTALLS_INSTALL_ID: OrgsOrgIdAppsInstallsInstallId,
        PathValues.ORGS_ORG_ID_APPS_INSTALLS_INSTALL_ID_SECRETS: OrgsOrgIdAppsInstallsInstallIdSecrets,
        PathValues.ORGS_ORG_ID_APPS_CLIENT_ID: OrgsOrgIdAppsClientId,
        PathValues.ORGS_ORG_ID_APPS_CLIENT_ID_SECRETS: OrgsOrgIdAppsClientIdSecrets,
        PathValues.ORGS_ORG_ID_AUDIT_LOGS_SEARCH: OrgsOrgIdAuditLogsSearch,
        PathValues.ORGS_ORG_ID_COLLECTIONS: OrgsOrgIdCollections,
        PathValues.ORGS_ORG_ID_COLLECTIONS_COLLECTION_ID: OrgsOrgIdCollectionsCollectionId,
        PathValues.ORGS_ORG_ID_COLLECTIONS_COLLECTION_ID_RELATIONSHIPS_PROJECTS: OrgsOrgIdCollectionsCollectionIdRelationshipsProjects,
        PathValues.ORGS_ORG_ID_CONTAINER_IMAGES: OrgsOrgIdContainerImages,
        PathValues.ORGS_ORG_ID_CONTAINER_IMAGES_IMAGE_ID: OrgsOrgIdContainerImagesImageId,
        PathValues.ORGS_ORG_ID_CONTAINER_IMAGES_IMAGE_ID_RELATIONSHIPS_IMAGE_TARGET_REFS: OrgsOrgIdContainerImagesImageIdRelationshipsImageTargetRefs,
        PathValues.ORGS_ORG_ID_INVITES: OrgsOrgIdInvites,
        PathValues.ORGS_ORG_ID_INVITES_INVITE_ID: OrgsOrgIdInvitesInviteId,
        PathValues.ORGS_ORG_ID_ISSUES: OrgsOrgIdIssues,
        PathValues.ORGS_ORG_ID_ISSUES_ISSUE_ID: OrgsOrgIdIssuesIssueId,
        PathValues.ORGS_ORG_ID_PACKAGES_ISSUES: OrgsOrgIdPackagesIssues,
        PathValues.ORGS_ORG_ID_PACKAGES_PURL_ISSUES: OrgsOrgIdPackagesPurlIssues,
        PathValues.ORGS_ORG_ID_PROJECTS: OrgsOrgIdProjects,
        PathValues.ORGS_ORG_ID_PROJECTS_PROJECT_ID: OrgsOrgIdProjectsProjectId,
        PathValues.ORGS_ORG_ID_PROJECTS_PROJECT_ID_SBOM: OrgsOrgIdProjectsProjectIdSbom,
        PathValues.ORGS_ORG_ID_SERVICE_ACCOUNTS: OrgsOrgIdServiceAccounts,
        PathValues.ORGS_ORG_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID: OrgsOrgIdServiceAccountsServiceaccountId,
        PathValues.ORGS_ORG_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID_SECRETS: OrgsOrgIdServiceAccountsServiceaccountIdSecrets,
        PathValues.ORGS_ORG_ID_SETTINGS_IAC: OrgsOrgIdSettingsIac,
        PathValues.ORGS_ORG_ID_SETTINGS_SAST: OrgsOrgIdSettingsSast,
        PathValues.ORGS_ORG_ID_SLACK_APP_BOT_ID: OrgsOrgIdSlackAppBotId,
        PathValues.ORGS_ORG_ID_SLACK_APP_BOT_ID_PROJECTS: OrgsOrgIdSlackAppBotIdProjects,
        PathValues.ORGS_ORG_ID_SLACK_APP_BOT_ID_PROJECTS_PROJECT_ID: OrgsOrgIdSlackAppBotIdProjectsProjectId,
        PathValues.ORGS_ORG_ID_SLACK_APP_TENANT_ID_CHANNELS: OrgsOrgIdSlackAppTenantIdChannels,
        PathValues.ORGS_ORG_ID_SLACK_APP_TENANT_ID_CHANNELS_CHANNEL_ID: OrgsOrgIdSlackAppTenantIdChannelsChannelId,
        PathValues.ORGS_ORG_ID_TARGETS: OrgsOrgIdTargets,
        PathValues.ORGS_ORG_ID_TARGETS_TARGET_ID: OrgsOrgIdTargetsTargetId,
        PathValues.SELF_APPS: SelfApps,
        PathValues.SELF_APPS_INSTALLS: SelfAppsInstalls,
        PathValues.SELF_APPS_INSTALLS_INSTALL_ID: SelfAppsInstallsInstallId,
        PathValues.SELF_APPS_APP_ID: SelfAppsAppId,
        PathValues.SELF_APPS_APP_ID_SESSIONS: SelfAppsAppIdSessions,
        PathValues.SELF_APPS_APP_ID_SESSIONS_SESSION_ID: SelfAppsAppIdSessionsSessionId,
    }
)
