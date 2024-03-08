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


RequiredServiceAccountsManageClientSecretResponseDataLinks = TypedDict("RequiredServiceAccountsManageClientSecretResponseDataLinks", {
    })

OptionalServiceAccountsManageClientSecretResponseDataLinks = TypedDict("OptionalServiceAccountsManageClientSecretResponseDataLinks", {
    "first": typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],

    "last": typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],

    "next": typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],

    "prev": typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],

    "related": typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],

    "self": typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]],
    }, total=False)

class ServiceAccountsManageClientSecretResponseDataLinks(RequiredServiceAccountsManageClientSecretResponseDataLinks, OptionalServiceAccountsManageClientSecretResponseDataLinks):
    pass
