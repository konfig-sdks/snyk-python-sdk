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

from snyk_python_sdk.pydantic.apps_delete_by_app_id409_response_errors_item import AppsDeleteByAppId409ResponseErrorsItem

AppsDeleteByAppId409ResponseErrors = typing.List[AppsDeleteByAppId409ResponseErrorsItem]
