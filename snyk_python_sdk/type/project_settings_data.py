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

from snyk_python_sdk.type.project_settings_data_attributes import ProjectSettingsDataAttributes

class RequiredProjectSettingsData(TypedDict):
    pass

class OptionalProjectSettingsData(TypedDict, total=False):
    attributes: ProjectSettingsDataAttributes

    id: str

    type: str

class ProjectSettingsData(RequiredProjectSettingsData, OptionalProjectSettingsData):
    pass