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

from snyk_python_sdk.pydantic.risk_factor_links import RiskFactorLinks

class DeployedRiskFactor(BaseModel):
    name: str = Field(alias='name')

    updated_at: datetime = Field(alias='updated_at')

    value: bool = Field(alias='value')

    included_in_score: typing.Optional[bool] = Field(None, alias='included_in_score')

    links: typing.Optional[RiskFactorLinks] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True
