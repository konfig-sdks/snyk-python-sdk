# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from snyk_python_sdk import schemas  # noqa: F401


class CommonIssueModelAttributesCoordinatesItemRemedies(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CommonIssueModelAttributesCoordinatesItemRemediesItem']:
            return CommonIssueModelAttributesCoordinatesItemRemediesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CommonIssueModelAttributesCoordinatesItemRemediesItem'], typing.List['CommonIssueModelAttributesCoordinatesItemRemediesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CommonIssueModelAttributesCoordinatesItemRemedies':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CommonIssueModelAttributesCoordinatesItemRemediesItem':
        return super().__getitem__(i)

from snyk_python_sdk.model.common_issue_model_attributes_coordinates_item_remedies_item import CommonIssueModelAttributesCoordinatesItemRemediesItem