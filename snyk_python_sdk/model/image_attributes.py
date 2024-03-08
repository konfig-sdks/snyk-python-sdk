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


class ImageAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "layers",
            "platform",
        }
        
        class properties:
            
            
            class layers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['ImageDigest']:
                        return ImageDigest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ImageDigest'], typing.List['ImageDigest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'layers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ImageDigest':
                    return super().__getitem__(i)
        
            @staticmethod
            def platform() -> typing.Type['Platform']:
                return Platform
            
            
            class names(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ImageName']:
                        return ImageName
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ImageName'], typing.List['ImageName']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'names':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ImageName':
                    return super().__getitem__(i)
            __annotations__ = {
                "layers": layers,
                "platform": platform,
                "names": names,
            }
    
    layers: MetaOapg.properties.layers
    platform: 'Platform'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layers"]) -> MetaOapg.properties.layers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> 'Platform': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["names"]) -> MetaOapg.properties.names: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["layers", "platform", "names", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layers"]) -> MetaOapg.properties.layers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> 'Platform': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["names"]) -> typing.Union[MetaOapg.properties.names, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["layers", "platform", "names", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        layers: typing.Union[MetaOapg.properties.layers, list, tuple, ],
        platform: 'Platform',
        names: typing.Union[MetaOapg.properties.names, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImageAttributes':
        return super().__new__(
            cls,
            *args,
            layers=layers,
            platform=platform,
            names=names,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.image_digest import ImageDigest
from snyk_python_sdk.model.image_name import ImageName
from snyk_python_sdk.model.platform import Platform
