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


class Region(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "start",
            "end",
        }
        
        class properties:
        
            @staticmethod
            def end() -> typing.Type['FilePosition']:
                return FilePosition
        
            @staticmethod
            def start() -> typing.Type['FilePosition']:
                return FilePosition
            __annotations__ = {
                "end": end,
                "start": start,
            }
    
    start: 'FilePosition'
    end: 'FilePosition'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> 'FilePosition': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> 'FilePosition': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["end", "start", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> 'FilePosition': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> 'FilePosition': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["end", "start", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        start: 'FilePosition',
        end: 'FilePosition',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Region':
        return super().__new__(
            cls,
            *args,
            start=start,
            end=end,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.file_position import FilePosition
