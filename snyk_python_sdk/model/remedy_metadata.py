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


class RemedyMetadata(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "schema_version",
            "data",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['RemedyMetadataData']:
                return RemedyMetadataData
            
            
            class schema_version(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 256
                    min_length = 1
            __annotations__ = {
                "data": data,
                "schema_version": schema_version,
            }
    
    schema_version: MetaOapg.properties.schema_version
    data: 'RemedyMetadataData'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'RemedyMetadataData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema_version"]) -> MetaOapg.properties.schema_version: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "schema_version", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'RemedyMetadataData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema_version"]) -> MetaOapg.properties.schema_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "schema_version", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        schema_version: typing.Union[MetaOapg.properties.schema_version, str, ],
        data: 'RemedyMetadataData',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RemedyMetadata':
        return super().__new__(
            cls,
            *args,
            schema_version=schema_version,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.remedy_metadata_data import RemedyMetadataData
