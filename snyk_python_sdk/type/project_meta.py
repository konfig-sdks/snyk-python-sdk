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


class RequiredProjectMeta(TypedDict):
    # The time the project was imported
    imported: datetime

    # The sum of critical severity issues of the project
    issues_critical_count: typing.Union[int, float]

    # The sum of high severity issues of the project
    issues_high_count: typing.Union[int, float]

    # The sum of low severity issues of the project
    issues_low_count: typing.Union[int, float]

    # The sum of medium severity issues of the project
    issues_medium_count: typing.Union[int, float]

    # The time the project was last tested
    last_tested_at: datetime

class OptionalProjectMeta(TypedDict, total=False):
    pass

class ProjectMeta(RequiredProjectMeta, OptionalProjectMeta):
    pass
