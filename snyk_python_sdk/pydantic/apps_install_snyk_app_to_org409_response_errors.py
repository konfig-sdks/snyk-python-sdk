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

from snyk_python_sdk.pydantic.apps_install_snyk_app_to_org409_response_errors_item import AppsInstallSnykAppToOrg409ResponseErrorsItem

AppsInstallSnykAppToOrg409ResponseErrors = typing.List[AppsInstallSnykAppToOrg409ResponseErrorsItem]
