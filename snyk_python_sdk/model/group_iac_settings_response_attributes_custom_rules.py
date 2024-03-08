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


class GroupIacSettingsResponseAttributesCustomRules(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Infrastructure as Code custom rules settings for a group.
    """


    class MetaOapg:
        
        class properties:
            is_enabled = schemas.BoolSchema
            oci_registry_tag = schemas.StrSchema
            oci_registry_url = schemas.StrSchema
            __annotations__ = {
                "is_enabled": is_enabled,
                "oci_registry_tag": oci_registry_tag,
                "oci_registry_url": oci_registry_url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oci_registry_tag"]) -> MetaOapg.properties.oci_registry_tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oci_registry_url"]) -> MetaOapg.properties.oci_registry_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_enabled", "oci_registry_tag", "oci_registry_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> typing.Union[MetaOapg.properties.is_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oci_registry_tag"]) -> typing.Union[MetaOapg.properties.oci_registry_tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oci_registry_url"]) -> typing.Union[MetaOapg.properties.oci_registry_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_enabled", "oci_registry_tag", "oci_registry_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, schemas.Unset] = schemas.unset,
        oci_registry_tag: typing.Union[MetaOapg.properties.oci_registry_tag, str, schemas.Unset] = schemas.unset,
        oci_registry_url: typing.Union[MetaOapg.properties.oci_registry_url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupIacSettingsResponseAttributesCustomRules':
        return super().__new__(
            cls,
            *args,
            is_enabled=is_enabled,
            oci_registry_tag=oci_registry_tag,
            oci_registry_url=oci_registry_url,
            _configuration=_configuration,
            **kwargs,
        )
