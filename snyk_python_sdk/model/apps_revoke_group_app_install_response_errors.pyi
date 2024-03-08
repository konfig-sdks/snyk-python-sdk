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


class AppsRevokeGroupAppInstallResponseErrors(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['AppsRevokeGroupAppInstallResponseErrorsItem']:
            return AppsRevokeGroupAppInstallResponseErrorsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['AppsRevokeGroupAppInstallResponseErrorsItem'], typing.List['AppsRevokeGroupAppInstallResponseErrorsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AppsRevokeGroupAppInstallResponseErrors':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'AppsRevokeGroupAppInstallResponseErrorsItem':
        return super().__getitem__(i)

from snyk_python_sdk.model.apps_revoke_group_app_install_response_errors_item import AppsRevokeGroupAppInstallResponseErrorsItem
