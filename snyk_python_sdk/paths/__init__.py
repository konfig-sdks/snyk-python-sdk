# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from snyk_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CUSTOM_BASE_IMAGES = "/custom_base_images"
    CUSTOM_BASE_IMAGES_CUSTOMBASEIMAGE_ID = "/custom_base_images/{custombaseimage_id}"
    GROUPS_GROUP_ID_APPS_INSTALLS = "/groups/{group_id}/apps/installs"
    GROUPS_GROUP_ID_APPS_INSTALLS_INSTALL_ID = "/groups/{group_id}/apps/installs/{install_id}"
    GROUPS_GROUP_ID_APPS_INSTALLS_INSTALL_ID_SECRETS = "/groups/{group_id}/apps/installs/{install_id}/secrets"
    GROUPS_GROUP_ID_AUDIT_LOGS_SEARCH = "/groups/{group_id}/audit_logs/search"
    GROUPS_GROUP_ID_ISSUES = "/groups/{group_id}/issues"
    GROUPS_GROUP_ID_ISSUES_ISSUE_ID = "/groups/{group_id}/issues/{issue_id}"
    GROUPS_GROUP_ID_ORGS = "/groups/{group_id}/orgs"
    GROUPS_GROUP_ID_SERVICE_ACCOUNTS = "/groups/{group_id}/service_accounts"
    GROUPS_GROUP_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID = "/groups/{group_id}/service_accounts/{serviceaccount_id}"
    GROUPS_GROUP_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID_SECRETS = "/groups/{group_id}/service_accounts/{serviceaccount_id}/secrets"
    GROUPS_GROUP_ID_SETTINGS_IAC = "/groups/{group_id}/settings/iac"
    OPENAPI = "/openapi"
    OPENAPI_VERSION = "/openapi/{version}"
    ORGS = "/orgs"
    ORGS_ORG_ID = "/orgs/{org_id}"
    ORGS_ORG_ID_APP_BOTS = "/orgs/{org_id}/app_bots"
    ORGS_ORG_ID_APP_BOTS_BOT_ID = "/orgs/{org_id}/app_bots/{bot_id}"
    ORGS_ORG_ID_APPS = "/orgs/{org_id}/apps"
    ORGS_ORG_ID_APPS_CREATIONS = "/orgs/{org_id}/apps/creations"
    ORGS_ORG_ID_APPS_CREATIONS_APP_ID = "/orgs/{org_id}/apps/creations/{app_id}"
    ORGS_ORG_ID_APPS_CREATIONS_APP_ID_SECRETS = "/orgs/{org_id}/apps/creations/{app_id}/secrets"
    ORGS_ORG_ID_APPS_INSTALLS = "/orgs/{org_id}/apps/installs"
    ORGS_ORG_ID_APPS_INSTALLS_INSTALL_ID = "/orgs/{org_id}/apps/installs/{install_id}"
    ORGS_ORG_ID_APPS_INSTALLS_INSTALL_ID_SECRETS = "/orgs/{org_id}/apps/installs/{install_id}/secrets"
    ORGS_ORG_ID_APPS_CLIENT_ID = "/orgs/{org_id}/apps/{client_id}"
    ORGS_ORG_ID_APPS_CLIENT_ID_SECRETS = "/orgs/{org_id}/apps/{client_id}/secrets"
    ORGS_ORG_ID_AUDIT_LOGS_SEARCH = "/orgs/{org_id}/audit_logs/search"
    ORGS_ORG_ID_COLLECTIONS = "/orgs/{org_id}/collections"
    ORGS_ORG_ID_COLLECTIONS_COLLECTION_ID = "/orgs/{org_id}/collections/{collection_id}"
    ORGS_ORG_ID_COLLECTIONS_COLLECTION_ID_RELATIONSHIPS_PROJECTS = "/orgs/{org_id}/collections/{collection_id}/relationships/projects"
    ORGS_ORG_ID_CONTAINER_IMAGES = "/orgs/{org_id}/container_images"
    ORGS_ORG_ID_CONTAINER_IMAGES_IMAGE_ID = "/orgs/{org_id}/container_images/{image_id}"
    ORGS_ORG_ID_CONTAINER_IMAGES_IMAGE_ID_RELATIONSHIPS_IMAGE_TARGET_REFS = "/orgs/{org_id}/container_images/{image_id}/relationships/image_target_refs"
    ORGS_ORG_ID_INVITES = "/orgs/{org_id}/invites"
    ORGS_ORG_ID_INVITES_INVITE_ID = "/orgs/{org_id}/invites/{invite_id}"
    ORGS_ORG_ID_ISSUES = "/orgs/{org_id}/issues"
    ORGS_ORG_ID_ISSUES_ISSUE_ID = "/orgs/{org_id}/issues/{issue_id}"
    ORGS_ORG_ID_PACKAGES_ISSUES = "/orgs/{org_id}/packages/issues"
    ORGS_ORG_ID_PACKAGES_PURL_ISSUES = "/orgs/{org_id}/packages/{purl}/issues"
    ORGS_ORG_ID_PROJECTS = "/orgs/{org_id}/projects"
    ORGS_ORG_ID_PROJECTS_PROJECT_ID = "/orgs/{org_id}/projects/{project_id}"
    ORGS_ORG_ID_PROJECTS_PROJECT_ID_SBOM = "/orgs/{org_id}/projects/{project_id}/sbom"
    ORGS_ORG_ID_SERVICE_ACCOUNTS = "/orgs/{org_id}/service_accounts"
    ORGS_ORG_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID = "/orgs/{org_id}/service_accounts/{serviceaccount_id}"
    ORGS_ORG_ID_SERVICE_ACCOUNTS_SERVICEACCOUNT_ID_SECRETS = "/orgs/{org_id}/service_accounts/{serviceaccount_id}/secrets"
    ORGS_ORG_ID_SETTINGS_IAC = "/orgs/{org_id}/settings/iac"
    ORGS_ORG_ID_SETTINGS_SAST = "/orgs/{org_id}/settings/sast"
    ORGS_ORG_ID_SLACK_APP_BOT_ID = "/orgs/{org_id}/slack_app/{bot_id}"
    ORGS_ORG_ID_SLACK_APP_BOT_ID_PROJECTS = "/orgs/{org_id}/slack_app/{bot_id}/projects"
    ORGS_ORG_ID_SLACK_APP_BOT_ID_PROJECTS_PROJECT_ID = "/orgs/{org_id}/slack_app/{bot_id}/projects/{project_id}"
    ORGS_ORG_ID_SLACK_APP_TENANT_ID_CHANNELS = "/orgs/{org_id}/slack_app/{tenant_id}/channels"
    ORGS_ORG_ID_SLACK_APP_TENANT_ID_CHANNELS_CHANNEL_ID = "/orgs/{org_id}/slack_app/{tenant_id}/channels/{channel_id}"
    ORGS_ORG_ID_TARGETS = "/orgs/{org_id}/targets"
    ORGS_ORG_ID_TARGETS_TARGET_ID = "/orgs/{org_id}/targets/{target_id}"
    SELF_APPS = "/self/apps"
    SELF_APPS_INSTALLS = "/self/apps/installs"
    SELF_APPS_INSTALLS_INSTALL_ID = "/self/apps/installs/{install_id}"
    SELF_APPS_APP_ID = "/self/apps/{app_id}"
    SELF_APPS_APP_ID_SESSIONS = "/self/apps/{app_id}/sessions"
    SELF_APPS_APP_ID_SESSIONS_SESSION_ID = "/self/apps/{app_id}/sessions/{session_id}"
