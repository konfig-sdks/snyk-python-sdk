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


class RequiredRiskScore(TypedDict):
    # Risk scoring model used to calculate the score value
    model: str

    # Risk score value, which may be used for overall prioritization
    value: int

class OptionalRiskScore(TypedDict, total=False):
    updated_at: datetime

class RiskScore(RequiredRiskScore, OptionalRiskScore):
    pass
