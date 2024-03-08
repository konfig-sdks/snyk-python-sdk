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

from snyk_python_sdk.pydantic.common_issue_model_attributes import CommonIssueModelAttributes

class CommonIssueModel(BaseModel):
    attributes: typing.Optional[CommonIssueModelAttributes] = Field(None, alias='attributes')

    # The Snyk ID of the vulnerability.
    id: typing.Optional[str] = Field(None, alias='id')

    # The type of the REST resource. Always ‘issue’.
    type: typing.Optional[str] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True