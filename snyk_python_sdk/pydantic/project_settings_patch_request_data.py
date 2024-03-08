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
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.project_settings_patch_request_data_attributes import ProjectSettingsPatchRequestDataAttributes

class ProjectSettingsPatchRequestData(BaseModel):
    attributes: ProjectSettingsPatchRequestDataAttributes = Field(alias='attributes')

    id: str = Field(alias='id')

    type: Literal["slack"] = Field(alias='type')
    class Config:
        arbitrary_types_allowed = True
