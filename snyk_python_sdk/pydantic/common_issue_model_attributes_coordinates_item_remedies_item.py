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

from snyk_python_sdk.pydantic.common_issue_model_attributes_coordinates_item_remedies_item_details import CommonIssueModelAttributesCoordinatesItemRemediesItemDetails

class CommonIssueModelAttributesCoordinatesItemRemediesItem(BaseModel):
    # A markdown-formatted optional description of this remedy.
    description: typing.Optional[str] = Field(None, alias='description')

    details: typing.Optional[CommonIssueModelAttributesCoordinatesItemRemediesItemDetails] = Field(None, alias='details')

    # The type of the remedy. Always ‘indeterminate’.
    type: typing.Optional[str] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
