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

from snyk_python_sdk.type.coordinate_v_two_remedies_item_details import CoordinateVTwoRemediesItemDetails

class RequiredCoordinateVTwoRemediesItem(TypedDict):
    pass

class OptionalCoordinateVTwoRemediesItem(TypedDict, total=False):
    # A markdown-formatted optional description of this remedy.
    description: str

    details: CoordinateVTwoRemediesItemDetails

    # The type of the remedy. Always ‘indeterminate’.
    type: str

class CoordinateVTwoRemediesItem(RequiredCoordinateVTwoRemediesItem, OptionalCoordinateVTwoRemediesItem):
    pass