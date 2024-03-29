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


class ServiceAccountsManageClientSecretForOrganizationServiceAccountRequestDataAttributes(BaseModel):
    # Operation to perform:   * `replace` - Replace existing secrets with a new generated secret.   * `create` - Add a new secret, preserving existing secrets. A maximum of to two secrets can exist at a time.   * `delete` - Remove an existing secret by value. At least one secret must remain per service account. 
    mode: Literal["replace", "create", "delete"] = Field(alias='mode')

    # Secret to delete when using `delete` mode
    secret: typing.Optional[str] = Field(None, alias='secret')
    class Config:
        arbitrary_types_allowed = True
