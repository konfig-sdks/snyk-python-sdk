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
from pydantic import BaseModel, Field, RootModel

from snyk_python_sdk.pydantic.slots_references import SlotsReferences

class Slots(BaseModel):
    # The time at which this vulnerability was disclosed.
    disclosure_time: typing.Optional[datetime] = Field(None, alias='disclosure_time')

    # The exploit maturity. Value of ‘No Data’, ‘Not Defined’, ‘Unproven’, ‘Proof of Concept’, ‘Functional’ or ‘High’.
    exploit: typing.Optional[str] = Field(None, alias='exploit')

    # The time at which this vulnerability was published.
    publication_time: typing.Optional[str] = Field(None, alias='publication_time')

    references: typing.Optional[SlotsReferences] = Field(None, alias='references')
    class Config:
        arbitrary_types_allowed = True
