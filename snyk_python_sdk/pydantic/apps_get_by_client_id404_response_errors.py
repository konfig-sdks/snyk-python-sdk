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

from snyk_python_sdk.pydantic.apps_get_by_client_id404_response_errors_item import AppsGetByClientId404ResponseErrorsItem

AppsGetByClientId404ResponseErrors = typing.List[AppsGetByClientId404ResponseErrorsItem]
