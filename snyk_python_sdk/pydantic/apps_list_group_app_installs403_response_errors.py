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

from snyk_python_sdk.pydantic.apps_list_group_app_installs403_response_errors_item import AppsListGroupAppInstalls403ResponseErrorsItem

AppsListGroupAppInstalls403ResponseErrors = typing.List[AppsListGroupAppInstalls403ResponseErrorsItem]
