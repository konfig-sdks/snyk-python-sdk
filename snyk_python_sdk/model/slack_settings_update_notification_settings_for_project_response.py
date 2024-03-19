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


class SlackSettingsUpdateNotificationSettingsForProjectResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def items() -> typing.Type['ProjectSettingsData']:
                return ProjectSettingsData
        
            @staticmethod
            def jsonapi() -> typing.Type['JsonApi']:
                return JsonApi
        
            @staticmethod
            def links() -> typing.Type['SelfLink']:
                return SelfLink
            __annotations__ = {
                "items": items,
                "jsonapi": jsonapi,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> 'ProjectSettingsData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jsonapi"]) -> 'JsonApi': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'SelfLink': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["items", "jsonapi", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union['ProjectSettingsData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jsonapi"]) -> typing.Union['JsonApi', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['SelfLink', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["items", "jsonapi", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        items: typing.Union['ProjectSettingsData', schemas.Unset] = schemas.unset,
        jsonapi: typing.Union['JsonApi', schemas.Unset] = schemas.unset,
        links: typing.Union['SelfLink', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SlackSettingsUpdateNotificationSettingsForProjectResponse':
        return super().__new__(
            cls,
            *args,
            items=items,
            jsonapi=jsonapi,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.json_api import JsonApi
from snyk_python_sdk.model.project_settings_data import ProjectSettingsData
from snyk_python_sdk.model.self_link import SelfLink
