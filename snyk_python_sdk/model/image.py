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


class Image(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "attributes",
            "id",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def attributes() -> typing.Type['ImageAttributes']:
                return ImageAttributes
        
            @staticmethod
            def id() -> typing.Type['ImageDigest']:
                return ImageDigest
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "container_image": "CONTAINER_IMAGE",
                    }
                
                @schemas.classproperty
                def CONTAINER_IMAGE(cls):
                    return cls("container_image")
        
            @staticmethod
            def relationships() -> typing.Type['ImageRelationships']:
                return ImageRelationships
            __annotations__ = {
                "attributes": attributes,
                "id": id,
                "type": type,
                "relationships": relationships,
            }
    
    attributes: 'ImageAttributes'
    id: 'ImageDigest'
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> 'ImageAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ImageDigest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> 'ImageRelationships': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", "relationships", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> 'ImageAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'ImageDigest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union['ImageRelationships', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", "relationships", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        attributes: 'ImageAttributes',
        id: 'ImageDigest',
        type: typing.Union[MetaOapg.properties.type, str, ],
        relationships: typing.Union['ImageRelationships', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Image':
        return super().__new__(
            cls,
            *args,
            attributes=attributes,
            id=id,
            type=type,
            relationships=relationships,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.image_attributes import ImageAttributes
from snyk_python_sdk.model.image_digest import ImageDigest
from snyk_python_sdk.model.image_relationships import ImageRelationships
