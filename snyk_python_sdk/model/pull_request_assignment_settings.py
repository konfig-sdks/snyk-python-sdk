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


class PullRequestAssignmentSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Automatically assign pull requests created by Snyk (limited to private repos). If not specified, settings will be inherited from the Project's integration.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def assignees() -> typing.Type['PullRequestAssignmentSettingsAssignees']:
                return PullRequestAssignmentSettingsAssignees
            is_enabled = schemas.BoolSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "auto": "AUTO",
                        "manual": "MANUAL",
                    }
                
                @schemas.classproperty
                def AUTO(cls):
                    return cls("auto")
                
                @schemas.classproperty
                def MANUAL(cls):
                    return cls("manual")
            __annotations__ = {
                "assignees": assignees,
                "is_enabled": is_enabled,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignees"]) -> 'PullRequestAssignmentSettingsAssignees': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assignees", "is_enabled", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignees"]) -> typing.Union['PullRequestAssignmentSettingsAssignees', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> typing.Union[MetaOapg.properties.is_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assignees", "is_enabled", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        assignees: typing.Union['PullRequestAssignmentSettingsAssignees', schemas.Unset] = schemas.unset,
        is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PullRequestAssignmentSettings':
        return super().__new__(
            cls,
            *args,
            assignees=assignees,
            is_enabled=is_enabled,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.pull_request_assignment_settings_assignees import PullRequestAssignmentSettingsAssignees
