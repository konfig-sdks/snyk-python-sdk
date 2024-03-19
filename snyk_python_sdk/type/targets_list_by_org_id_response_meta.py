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


class RequiredTargetsListByOrgIdResponseMeta(TypedDict):
    pass

class OptionalTargetsListByOrgIdResponseMeta(TypedDict, total=False):
    count: typing.Union[int, float]

class TargetsListByOrgIdResponseMeta(RequiredTargetsListByOrgIdResponseMeta, OptionalTargetsListByOrgIdResponseMeta):
    pass
