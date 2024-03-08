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


class CollectionAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
        
            @staticmethod
            def name() -> typing.Type['Name']:
                return Name
            is_generated = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "is_generated": is_generated,
            }
    
    name: 'Name'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_generated"]) -> MetaOapg.properties.is_generated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "is_generated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> 'Name': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_generated"]) -> typing.Union[MetaOapg.properties.is_generated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "is_generated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: 'Name',
        is_generated: typing.Union[MetaOapg.properties.is_generated, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CollectionAttributes':
        return super().__new__(
            cls,
            *args,
            name=name,
            is_generated=is_generated,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.name import Name