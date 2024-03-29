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


class ProjectSettingsDataAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "target_channel_name",
            "target_project_name",
            "is_active",
            "target_channel_id",
            "severity_threshold",
        }
        
        class properties:
            is_active = schemas.BoolSchema
        
            @staticmethod
            def severity_threshold() -> typing.Type['SeverityThreshold']:
                return SeverityThreshold
            target_channel_id = schemas.StrSchema
        
            @staticmethod
            def target_channel_name() -> typing.Type['TargetChannelName']:
                return TargetChannelName
            target_project_name = schemas.StrSchema
            __annotations__ = {
                "is_active": is_active,
                "severity_threshold": severity_threshold,
                "target_channel_id": target_channel_id,
                "target_channel_name": target_channel_name,
                "target_project_name": target_project_name,
            }
    
    target_channel_name: 'TargetChannelName'
    target_project_name: MetaOapg.properties.target_project_name
    is_active: MetaOapg.properties.is_active
    target_channel_id: MetaOapg.properties.target_channel_id
    severity_threshold: 'SeverityThreshold'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity_threshold"]) -> 'SeverityThreshold': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_channel_id"]) -> MetaOapg.properties.target_channel_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_channel_name"]) -> 'TargetChannelName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_project_name"]) -> MetaOapg.properties.target_project_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_active", "severity_threshold", "target_channel_id", "target_channel_name", "target_project_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity_threshold"]) -> 'SeverityThreshold': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_channel_id"]) -> MetaOapg.properties.target_channel_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_channel_name"]) -> 'TargetChannelName': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_project_name"]) -> MetaOapg.properties.target_project_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_active", "severity_threshold", "target_channel_id", "target_channel_name", "target_project_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        target_channel_name: 'TargetChannelName',
        target_project_name: typing.Union[MetaOapg.properties.target_project_name, str, ],
        is_active: typing.Union[MetaOapg.properties.is_active, bool, ],
        target_channel_id: typing.Union[MetaOapg.properties.target_channel_id, str, ],
        severity_threshold: 'SeverityThreshold',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectSettingsDataAttributes':
        return super().__new__(
            cls,
            *args,
            target_channel_name=target_channel_name,
            target_project_name=target_project_name,
            is_active=is_active,
            target_channel_id=target_channel_id,
            severity_threshold=severity_threshold,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.severity_threshold import SeverityThreshold
from snyk_python_sdk.model.target_channel_name import TargetChannelName
