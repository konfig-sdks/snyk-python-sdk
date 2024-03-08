# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from snyk_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    APPS = "Apps"
    SERVICE_ACCOUNTS = "ServiceAccounts"
    COLLECTION = "Collection"
    SLACK_SETTINGS = "SlackSettings"
    ISSUES = "Issues"
    CUSTOM_BASE_IMAGES = "Custom Base Images"
    IAC_SETTINGS = "IacSettings"
    ORGS = "Orgs"
    PROJECTS = "Projects"
    CONTAINER_IMAGE = "ContainerImage"
    INVITES = "Invites"
    TARGETS = "Targets"
    AUDIT_LOGS = "Audit Logs"
    OPEN_API = "OpenAPI"
    SAST_SETTINGS = "SastSettings"
    SLACK = "Slack"
    SBOM = "SBOM"
    EXAMPLES = "Examples"
