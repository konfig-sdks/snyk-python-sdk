# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

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


class IssuesGetById403ResponseErrors(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        min_items = 1
        
        @staticmethod
        def items() -> typing.Type['IssuesGetById403ResponseErrorsItem']:
            return IssuesGetById403ResponseErrorsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['IssuesGetById403ResponseErrorsItem'], typing.List['IssuesGetById403ResponseErrorsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IssuesGetById403ResponseErrors':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'IssuesGetById403ResponseErrorsItem':
        return super().__getitem__(i)

from snyk_python_sdk.model.issues_get_by_id403_response_errors_item import IssuesGetById403ResponseErrorsItem
