# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from snyk_python_sdk.type.severity_threshold import SeverityThreshold
from snyk_python_sdk.type.target_channel_name import TargetChannelName

class RequiredProjectSettingsDataAttributes(TypedDict):
    # Current status of the project settings.
    is_active: bool

    severity_threshold: SeverityThreshold

    target_channel_id: str

    target_channel_name: TargetChannelName

    # The target file name for the project.
    target_project_name: str

class OptionalProjectSettingsDataAttributes(TypedDict, total=False):
    pass

class ProjectSettingsDataAttributes(RequiredProjectSettingsDataAttributes, OptionalProjectSettingsDataAttributes):
    pass