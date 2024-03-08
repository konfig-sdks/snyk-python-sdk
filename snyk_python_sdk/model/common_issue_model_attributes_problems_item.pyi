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


class CommonIssueModelAttributesProblemsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "id",
            "source",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class source(
                schemas.StrSchema
            ):
                pass
            disclosed_at = schemas.DateTimeSchema
            discovered_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            
            
            class url(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "id": id,
                "source": source,
                "disclosed_at": disclosed_at,
                "discovered_at": discovered_at,
                "updated_at": updated_at,
                "url": url,
            }
    
    id: MetaOapg.properties.id
    source: MetaOapg.properties.source
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disclosed_at"]) -> MetaOapg.properties.disclosed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discovered_at"]) -> MetaOapg.properties.discovered_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "source", "disclosed_at", "discovered_at", "updated_at", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disclosed_at"]) -> typing.Union[MetaOapg.properties.disclosed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discovered_at"]) -> typing.Union[MetaOapg.properties.discovered_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "source", "disclosed_at", "discovered_at", "updated_at", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        source: typing.Union[MetaOapg.properties.source, str, ],
        disclosed_at: typing.Union[MetaOapg.properties.disclosed_at, str, datetime, schemas.Unset] = schemas.unset,
        discovered_at: typing.Union[MetaOapg.properties.discovered_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CommonIssueModelAttributesProblemsItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            source=source,
            disclosed_at=disclosed_at,
            discovered_at=discovered_at,
            updated_at=updated_at,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )
