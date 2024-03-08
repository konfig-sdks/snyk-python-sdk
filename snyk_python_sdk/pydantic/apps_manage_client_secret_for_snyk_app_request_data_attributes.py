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


class AppsManageClientSecretForSnykAppRequestDataAttributes(BaseModel):
    # Operation to perform:   * `replace` - Replace existing secrets with a new generated secret   * `create` - Add a new secret, preserving existing secrets   * `delete` - Remove an existing secret by value 
    mode: Literal["replace", "create", "delete"] = Field(alias='mode')

    # Secret to delete when using `delete` mode
    secret: typing.Optional[str] = Field(None, alias='secret')
    class Config:
        arbitrary_types_allowed = True
