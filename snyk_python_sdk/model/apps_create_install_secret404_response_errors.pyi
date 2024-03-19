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


class AppsCreateInstallSecret404ResponseErrors(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['AppsCreateInstallSecret404ResponseErrorsItem']:
            return AppsCreateInstallSecret404ResponseErrorsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['AppsCreateInstallSecret404ResponseErrorsItem'], typing.List['AppsCreateInstallSecret404ResponseErrorsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AppsCreateInstallSecret404ResponseErrors':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'AppsCreateInstallSecret404ResponseErrorsItem':
        return super().__getitem__(i)

from snyk_python_sdk.model.apps_create_install_secret404_response_errors_item import AppsCreateInstallSecret404ResponseErrorsItem
