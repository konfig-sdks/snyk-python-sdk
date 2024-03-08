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


class ManualRemediationPRsSettings(BaseModel):
    # Include vulnerability patches in manual pull requests.
    is_patch_remediation_enabled: typing.Optional[bool] = Field(None, alias='is_patch_remediation_enabled')
    class Config:
        arbitrary_types_allowed = True
