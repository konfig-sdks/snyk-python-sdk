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

from snyk_python_sdk.pydantic.apps_by_install_id500_response_errors_item import AppsByInstallId500ResponseErrorsItem

AppsByInstallId500ResponseErrors = typing.List[AppsByInstallId500ResponseErrorsItem]
