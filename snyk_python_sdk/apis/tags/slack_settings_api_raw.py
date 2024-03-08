# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from snyk_python_sdk.paths.orgs_org_id_slack_app_bot_id.post import CreateDefaultNotificationSettingsRaw
from snyk_python_sdk.paths.orgs_org_id_slack_app_bot_id.get import GetDefaultNotificationSettingsRaw
from snyk_python_sdk.paths.orgs_org_id_slack_app_bot_id_projects.get import GetOverridesForProjectsRaw
from snyk_python_sdk.paths.orgs_org_id_slack_app_bot_id_projects_project_id.post import ProjectOverrideRaw
from snyk_python_sdk.paths.orgs_org_id_slack_app_bot_id.delete import RemoveIntegrationRaw
from snyk_python_sdk.paths.orgs_org_id_slack_app_bot_id_projects_project_id.delete import RemoveProjectOverrideRaw
from snyk_python_sdk.paths.orgs_org_id_slack_app_bot_id_projects_project_id.patch import UpdateNotificationSettingsForProjectRaw


class SlackSettingsApiRaw(
    CreateDefaultNotificationSettingsRaw,
    GetDefaultNotificationSettingsRaw,
    GetOverridesForProjectsRaw,
    ProjectOverrideRaw,
    RemoveIntegrationRaw,
    RemoveProjectOverrideRaw,
    UpdateNotificationSettingsForProjectRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
