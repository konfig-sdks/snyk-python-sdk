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

from snyk_python_sdk.pydantic.apps_revoke_by_install_id401_response_errors import AppsRevokeByInstallId401ResponseErrors
from snyk_python_sdk.pydantic.apps_revoke_by_install_id401_response_jsonapi import AppsRevokeByInstallId401ResponseJsonapi

class AppsRevokeByInstallId401Response(BaseModel):
    errors: AppsRevokeByInstallId401ResponseErrors = Field(alias='errors')

    jsonapi: AppsRevokeByInstallId401ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
