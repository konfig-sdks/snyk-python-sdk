# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.patch_project_request_data_attributes_business_criticality import PatchProjectRequestDataAttributesBusinessCriticality
from snyk_python_sdk.pydantic.patch_project_request_data_attributes_environment import PatchProjectRequestDataAttributesEnvironment
from snyk_python_sdk.pydantic.patch_project_request_data_attributes_lifecycle import PatchProjectRequestDataAttributesLifecycle
from snyk_python_sdk.pydantic.patch_project_request_data_attributes_tags import PatchProjectRequestDataAttributesTags

class PatchProjectRequestDataAttributes(BaseModel):
    tags: typing.Optional[PatchProjectRequestDataAttributesTags] = Field(None, alias='tags')

    business_criticality: typing.Optional[PatchProjectRequestDataAttributesBusinessCriticality] = Field(None, alias='business_criticality')

    environment: typing.Optional[PatchProjectRequestDataAttributesEnvironment] = Field(None, alias='environment')

    lifecycle: typing.Optional[PatchProjectRequestDataAttributesLifecycle] = Field(None, alias='lifecycle')

    # Test frequency of a project. Also controls when automated PRs may be created.
    test_frequency: typing.Optional[Literal["daily", "weekly", "never"]] = Field(None, alias='test_frequency')
    class Config:
        arbitrary_types_allowed = True
