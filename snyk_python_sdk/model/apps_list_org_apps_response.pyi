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


class AppsListOrgAppsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "jsonapi",
            "data",
            "links",
        }
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AppData']:
                        return AppData
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AppData'], typing.List['AppData']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AppData':
                    return super().__getitem__(i)
        
            @staticmethod
            def jsonapi() -> typing.Type['JsonApi']:
                return JsonApi
        
            @staticmethod
            def links() -> typing.Type['PaginatedLinks']:
                return PaginatedLinks
            __annotations__ = {
                "data": data,
                "jsonapi": jsonapi,
                "links": links,
            }
    
    jsonapi: 'JsonApi'
    data: MetaOapg.properties.data
    links: 'PaginatedLinks'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jsonapi"]) -> 'JsonApi': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'PaginatedLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "jsonapi", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jsonapi"]) -> 'JsonApi': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> 'PaginatedLinks': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "jsonapi", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jsonapi: 'JsonApi',
        data: typing.Union[MetaOapg.properties.data, list, tuple, ],
        links: 'PaginatedLinks',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsListOrgAppsResponse':
        return super().__new__(
            cls,
            *args,
            jsonapi=jsonapi,
            data=data,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.app_data import AppData
from snyk_python_sdk.model.json_api import JsonApi
from snyk_python_sdk.model.paginated_links import PaginatedLinks
