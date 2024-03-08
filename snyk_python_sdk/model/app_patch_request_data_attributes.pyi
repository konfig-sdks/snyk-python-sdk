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


class AppPatchRequestDataAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def access_token_ttl_seconds() -> typing.Type['AccessTokenTtlSeconds']:
                return AccessTokenTtlSeconds
        
            @staticmethod
            def name() -> typing.Type['AppName']:
                return AppName
        
            @staticmethod
            def redirect_uris() -> typing.Type['RedirectUris']:
                return RedirectUris
            __annotations__ = {
                "access_token_ttl_seconds": access_token_ttl_seconds,
                "name": name,
                "redirect_uris": redirect_uris,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token_ttl_seconds"]) -> 'AccessTokenTtlSeconds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'AppName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_uris"]) -> 'RedirectUris': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access_token_ttl_seconds", "name", "redirect_uris", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token_ttl_seconds"]) -> typing.Union['AccessTokenTtlSeconds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['AppName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_uris"]) -> typing.Union['RedirectUris', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access_token_ttl_seconds", "name", "redirect_uris", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access_token_ttl_seconds: typing.Union['AccessTokenTtlSeconds', schemas.Unset] = schemas.unset,
        name: typing.Union['AppName', schemas.Unset] = schemas.unset,
        redirect_uris: typing.Union['RedirectUris', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppPatchRequestDataAttributes':
        return super().__new__(
            cls,
            *args,
            access_token_ttl_seconds=access_token_ttl_seconds,
            name=name,
            redirect_uris=redirect_uris,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.access_token_ttl_seconds import AccessTokenTtlSeconds
from snyk_python_sdk.model.app_name import AppName
from snyk_python_sdk.model.redirect_uris import RedirectUris