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


class AppsGetActiveSessions500Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "jsonapi",
            "errors",
        }
        
        class properties:
        
            @staticmethod
            def errors() -> typing.Type['AppsGetActiveSessions500ResponseErrors']:
                return AppsGetActiveSessions500ResponseErrors
        
            @staticmethod
            def jsonapi() -> typing.Type['AppsGetActiveSessions500ResponseJsonapi']:
                return AppsGetActiveSessions500ResponseJsonapi
            __annotations__ = {
                "errors": errors,
                "jsonapi": jsonapi,
            }
    
    jsonapi: 'AppsGetActiveSessions500ResponseJsonapi'
    errors: 'AppsGetActiveSessions500ResponseErrors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'AppsGetActiveSessions500ResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jsonapi"]) -> 'AppsGetActiveSessions500ResponseJsonapi': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'AppsGetActiveSessions500ResponseErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jsonapi"]) -> 'AppsGetActiveSessions500ResponseJsonapi': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jsonapi: 'AppsGetActiveSessions500ResponseJsonapi',
        errors: 'AppsGetActiveSessions500ResponseErrors',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsGetActiveSessions500Response':
        return super().__new__(
            cls,
            *args,
            jsonapi=jsonapi,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.apps_get_active_sessions500_response_errors import AppsGetActiveSessions500ResponseErrors
from snyk_python_sdk.model.apps_get_active_sessions500_response_jsonapi import AppsGetActiveSessions500ResponseJsonapi
