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


class RequiredLatestDependencyTotal(TypedDict):
    pass

class OptionalLatestDependencyTotal(TypedDict, total=False):
    total: typing.Union[int, float]

    updated_at: datetime

class LatestDependencyTotal(RequiredLatestDependencyTotal, OptionalLatestDependencyTotal):
    pass
