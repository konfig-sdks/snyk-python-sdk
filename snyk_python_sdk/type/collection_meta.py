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


class RequiredCollectionMeta(TypedDict):
    # The sum of critical severity issues of the collection's projects
    issues_critical_count: typing.Union[int, float]

    # The sum of high severity issues of the collection's projects
    issues_high_count: typing.Union[int, float]

    # The sum of low severity issues of the collection's projects
    issues_low_count: typing.Union[int, float]

    # The sum of medium severity issues of the collection's projects
    issues_medium_count: typing.Union[int, float]

    # The amount of projects belonging to this collection
    projects_count: typing.Union[int, float]

class OptionalCollectionMeta(TypedDict, total=False):
    pass

class CollectionMeta(RequiredCollectionMeta, OptionalCollectionMeta):
    pass