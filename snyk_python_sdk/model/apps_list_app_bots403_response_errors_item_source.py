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


class AppsListAppBots403ResponseErrorsItemSource(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            parameter = schemas.StrSchema
            pointer = schemas.StrSchema
            __annotations__ = {
                "parameter": parameter,
                "pointer": pointer,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameter"]) -> MetaOapg.properties.parameter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointer"]) -> MetaOapg.properties.pointer: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["parameter", "pointer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameter"]) -> typing.Union[MetaOapg.properties.parameter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointer"]) -> typing.Union[MetaOapg.properties.pointer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parameter", "pointer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        parameter: typing.Union[MetaOapg.properties.parameter, str, schemas.Unset] = schemas.unset,
        pointer: typing.Union[MetaOapg.properties.pointer, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsListAppBots403ResponseErrorsItemSource':
        return super().__new__(
            cls,
            *args,
            parameter=parameter,
            pointer=pointer,
            _configuration=_configuration,
            **kwargs,
        )
