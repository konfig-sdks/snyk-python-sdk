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

from snyk_python_sdk.pydantic.json_api import JsonApi
from snyk_python_sdk.pydantic.links import Links
from snyk_python_sdk.pydantic.public_target import PublicTarget
from snyk_python_sdk.pydantic.targets_list_by_org_id_response_meta import TargetsListByOrgIdResponseMeta

class TargetsListByOrgIdResponse(BaseModel):
    data: typing.List[PublicTarget] = Field(alias='data')

    jsonapi: JsonApi = Field(alias='jsonapi')

    links: Links = Field(alias='links')

    meta: typing.Optional[TargetsListByOrgIdResponseMeta] = Field(None, alias='meta')
    class Config:
        arbitrary_types_allowed = True
