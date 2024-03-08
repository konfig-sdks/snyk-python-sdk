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


class AppsListUserInstalledApps500ResponseErrorsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "detail",
            "status",
        }
        
        class properties:
            detail = schemas.StrSchema
            
            
            class status(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[45]\d\d$',
                    }]
            title = schemas.StrSchema
            code = schemas.StrSchema
            id = schemas.UUIDSchema
        
            @staticmethod
            def meta() -> typing.Type['AppsListUserInstalledApps500ResponseErrorsItemMeta']:
                return AppsListUserInstalledApps500ResponseErrorsItemMeta
        
            @staticmethod
            def source() -> typing.Type['AppsListUserInstalledApps500ResponseErrorsItemSource']:
                return AppsListUserInstalledApps500ResponseErrorsItemSource
            __annotations__ = {
                "detail": detail,
                "status": status,
                "title": title,
                "code": code,
                "id": id,
                "meta": meta,
                "source": source,
            }
    
    detail: MetaOapg.properties.detail
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'AppsListUserInstalledApps500ResponseErrorsItemMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'AppsListUserInstalledApps500ResponseErrorsItemSource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["detail", "status", "title", "code", "id", "meta", "source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['AppsListUserInstalledApps500ResponseErrorsItemMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union['AppsListUserInstalledApps500ResponseErrorsItemSource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["detail", "status", "title", "code", "id", "meta", "source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        detail: typing.Union[MetaOapg.properties.detail, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        meta: typing.Union['AppsListUserInstalledApps500ResponseErrorsItemMeta', schemas.Unset] = schemas.unset,
        source: typing.Union['AppsListUserInstalledApps500ResponseErrorsItemSource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsListUserInstalledApps500ResponseErrorsItem':
        return super().__new__(
            cls,
            *args,
            detail=detail,
            status=status,
            title=title,
            code=code,
            id=id,
            meta=meta,
            source=source,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.apps_list_user_installed_apps500_response_errors_item_meta import AppsListUserInstalledApps500ResponseErrorsItemMeta
from snyk_python_sdk.model.apps_list_user_installed_apps500_response_errors_item_source import AppsListUserInstalledApps500ResponseErrorsItemSource
