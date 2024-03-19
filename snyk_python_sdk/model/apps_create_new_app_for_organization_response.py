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


class AppsCreateNewAppForOrganizationResponse(
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
            def errors() -> typing.Type['AppsCreateNewAppForOrganizationResponseErrors']:
                return AppsCreateNewAppForOrganizationResponseErrors
        
            @staticmethod
            def jsonapi() -> typing.Type['AppsCreateNewAppForOrganizationResponseJsonapi']:
                return AppsCreateNewAppForOrganizationResponseJsonapi
            __annotations__ = {
                "errors": errors,
                "jsonapi": jsonapi,
            }
    
    jsonapi: 'AppsCreateNewAppForOrganizationResponseJsonapi'
    errors: 'AppsCreateNewAppForOrganizationResponseErrors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'AppsCreateNewAppForOrganizationResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jsonapi"]) -> 'AppsCreateNewAppForOrganizationResponseJsonapi': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'AppsCreateNewAppForOrganizationResponseErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jsonapi"]) -> 'AppsCreateNewAppForOrganizationResponseJsonapi': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jsonapi: 'AppsCreateNewAppForOrganizationResponseJsonapi',
        errors: 'AppsCreateNewAppForOrganizationResponseErrors',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsCreateNewAppForOrganizationResponse':
        return super().__new__(
            cls,
            *args,
            jsonapi=jsonapi,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.apps_create_new_app_for_organization_response_errors import AppsCreateNewAppForOrganizationResponseErrors
from snyk_python_sdk.model.apps_create_new_app_for_organization_response_jsonapi import AppsCreateNewAppForOrganizationResponseJsonapi
