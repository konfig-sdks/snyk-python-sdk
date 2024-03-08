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

from snyk_python_sdk.type.slots_references import SlotsReferences

class RequiredSlots(TypedDict):
    pass

class OptionalSlots(TypedDict, total=False):
    # The time at which this vulnerability was disclosed.
    disclosure_time: datetime

    # The exploit maturity. Value of ‘No Data’, ‘Not Defined’, ‘Unproven’, ‘Proof of Concept’, ‘Functional’ or ‘High’.
    exploit: str

    # The time at which this vulnerability was published.
    publication_time: str

    references: SlotsReferences

class Slots(RequiredSlots, OptionalSlots):
    pass