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

from snyk_python_sdk.type.link_property import LinkProperty

class RequiredRiskFactorLinks(TypedDict):
    pass

class OptionalRiskFactorLinks(TypedDict, total=False):
    evidence: LinkProperty

class RiskFactorLinks(RequiredRiskFactorLinks, OptionalRiskFactorLinks):
    pass
