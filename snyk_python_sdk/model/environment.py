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


class Environment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "id",
            "type",
        }
        
        class properties:
            id = schemas.UUIDSchema
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 256
                    min_length = 1
        
            @staticmethod
            def type() -> typing.Type['EnvironmentTypeDef']:
                return EnvironmentTypeDef
            
            
            class native_id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 2048
                    min_length = 1
            __annotations__ = {
                "id": id,
                "name": name,
                "type": type,
                "native_id": native_id,
            }
    
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    type: 'EnvironmentTypeDef'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'EnvironmentTypeDef': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["native_id"]) -> MetaOapg.properties.native_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "native_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'EnvironmentTypeDef': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["native_id"]) -> typing.Union[MetaOapg.properties.native_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "native_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        type: 'EnvironmentTypeDef',
        native_id: typing.Union[MetaOapg.properties.native_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Environment':
        return super().__new__(
            cls,
            *args,
            name=name,
            id=id,
            type=type,
            native_id=native_id,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.environment_type_def import EnvironmentTypeDef
