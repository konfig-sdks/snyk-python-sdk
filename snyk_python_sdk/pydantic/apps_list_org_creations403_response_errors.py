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

from snyk_python_sdk.pydantic.apps_list_org_creations403_response_errors_item import AppsListOrgCreations403ResponseErrorsItem

AppsListOrgCreations403ResponseErrors = typing.List[AppsListOrgCreations403ResponseErrorsItem]
