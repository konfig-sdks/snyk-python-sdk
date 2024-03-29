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

from snyk_python_sdk.pydantic.apps_create_install_secret409_response_errors import AppsCreateInstallSecret409ResponseErrors
from snyk_python_sdk.pydantic.apps_create_install_secret409_response_jsonapi import AppsCreateInstallSecret409ResponseJsonapi

class AppsCreateInstallSecret409Response(BaseModel):
    errors: AppsCreateInstallSecret409ResponseErrors = Field(alias='errors')

    jsonapi: AppsCreateInstallSecret409ResponseJsonapi = Field(alias='jsonapi')
    class Config:
        arbitrary_types_allowed = True
