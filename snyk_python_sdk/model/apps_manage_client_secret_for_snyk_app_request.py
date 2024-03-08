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


class AppsManageClientSecretForSnykAppRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "data",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['AppsManageClientSecretForSnykAppRequestData']:
                return AppsManageClientSecretForSnykAppRequestData
            __annotations__ = {
                "data": data,
            }
    
    data: 'AppsManageClientSecretForSnykAppRequestData'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'AppsManageClientSecretForSnykAppRequestData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'AppsManageClientSecretForSnykAppRequestData': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: 'AppsManageClientSecretForSnykAppRequestData',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsManageClientSecretForSnykAppRequest':
        return super().__new__(
            cls,
            *args,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.apps_manage_client_secret_for_snyk_app_request_data import AppsManageClientSecretForSnykAppRequestData
