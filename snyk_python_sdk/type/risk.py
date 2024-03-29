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

from snyk_python_sdk.type.risk_factor import RiskFactor
from snyk_python_sdk.type.risk_score import RiskScore

class RequiredRisk(TypedDict):
    # Risk factors identified for an issue
    factors: typing.List[RiskFactor]

class OptionalRisk(TypedDict, total=False):
    score: RiskScore

class Risk(RequiredRisk, OptionalRisk):
    pass
