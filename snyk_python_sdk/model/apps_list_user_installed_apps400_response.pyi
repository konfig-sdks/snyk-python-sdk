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


class AppsListUserInstalledApps400Response(
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
            def errors() -> typing.Type['AppsListUserInstalledApps400ResponseErrors']:
                return AppsListUserInstalledApps400ResponseErrors
        
            @staticmethod
            def jsonapi() -> typing.Type['AppsListUserInstalledApps400ResponseJsonapi']:
                return AppsListUserInstalledApps400ResponseJsonapi
            __annotations__ = {
                "errors": errors,
                "jsonapi": jsonapi,
            }
    
    jsonapi: 'AppsListUserInstalledApps400ResponseJsonapi'
    errors: 'AppsListUserInstalledApps400ResponseErrors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'AppsListUserInstalledApps400ResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jsonapi"]) -> 'AppsListUserInstalledApps400ResponseJsonapi': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'AppsListUserInstalledApps400ResponseErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jsonapi"]) -> 'AppsListUserInstalledApps400ResponseJsonapi': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jsonapi: 'AppsListUserInstalledApps400ResponseJsonapi',
        errors: 'AppsListUserInstalledApps400ResponseErrors',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsListUserInstalledApps400Response':
        return super().__new__(
            cls,
            *args,
            jsonapi=jsonapi,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.apps_list_user_installed_apps400_response_errors import AppsListUserInstalledApps400ResponseErrors
from snyk_python_sdk.model.apps_list_user_installed_apps400_response_jsonapi import AppsListUserInstalledApps400ResponseJsonapi
